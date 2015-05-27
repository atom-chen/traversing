# -*- coding:utf-8 -*-
"""
created by server on 14-8-12下午2:17.
"""
from gfirefly.server.globalobject import remoteserviceHandle
from shared.db_opear.configs_data import game_configs
from app.proto_file.common_pb2 import CommonResponse
from gfirefly.server.globalobject import GlobalObject
from app.proto_file import hjqy_pb2
from gfirefly.server.logobj import logger
from app.game.core.item_group_helper import gain, get_return
from shared.utils.const import const
from app.game.action.node._fight_start_logic import save_line_up_order
from app.game.action.node._fight_start_logic import pvp_assemble_units
from app.game.action.node._fight_start_logic import get_seeds
from shared.utils.date_util import is_in_period

remote_gate = GlobalObject().remote.get('gate')


@remoteserviceHandle('gate')
def init_2101(pro_data, player):
    """获取hjqy信息
    """
    response = hjqy_pb2.HjqyInitResponse()
    friend_ids = player.friends.friends
    data = remote_gate['world'].hjqy_init_remote(player.base_info.id, friend_ids)
    for boss_data in data.values():
        construct_boss_pb(data, response)

    data.damage_hp = remote_gate['world'].hjqy_damage_hp_remote(player.base_info.id)
    return response.SerializeToString()

def construct_boss_pb(data, response):
    """docstring for construct_boss_pb"""
    boss_pb = response.data.add()
    boss_pb.player_id = data.get("player_id")
    boss_pb.stage_id = data.get("stage_id")
    boss_pb.is_share = data.get("is_share")
    boss_pb.trigger_time = data.get("trigger_time")
    boss_pb.hp_max = data.get("hp_max")
    boss_pb.hp_left = data.get("hp_left")
    #boss_pb.damage_hp = data.get("damage_hp")
    boss_pb.state = data.get("state")


    #required int32 player_id = 1;     // 触发boss的玩家id
    #required int32 stage_id = 4;      // 关卡id
    #required bool is_share = 3;       // 是否分享给好友
    #optional bool open_or_not = 8;    // 是否开启, no:上面参数有效，yes：下面参数有效
    #optional int32 hp_left = 9;       // 剩余血量
    #optional int32 demage_hp = 10;    // 伤害
    #optional int32 rank_no = 11;      // 名次
    #optional int32 fight_times = 12;  // 战斗次数
    #optional int32 hp_max = 13;       // boss最大血量
    #optional int32 trigger_time = 14; // 触发时间

@remoteserviceHandle('gate')
def share_2102(pro_data, player):
    """分享hjqy, 广播协议号2112
    """
    response = CommonResponse()
    result = remote_gate['world'].share_hjqy_remote(player.base_info.id)
    response.result = result
    return response.SerializeToString()



@remoteserviceHandle('gate')
def battle_2103(pro_data, player):
    """
    开始战斗
    request:HjqyBattleRequest
    response:HjqyBattleResponse
    """
    request = hjqy_pb2.HjqyBattleRequest()
    request.ParseFromString(pro_data)
    response = hjqy_pb2.HjqyBattleResponse()

    boss_id = request.owner_id
    line_up = request.line_up
    attack_type = request.attack_type # 全力一击，普通攻击

    hjqyExchangeBUFFTime = game_configs.base_config.get("hjqyExchangeBUFFTime")
    hjqyItemRate = game_configs.base_config.get("hjqyItemRate")

    need_hjqy_coin = 1
    if attack_type == 2:
        need_hjqy_coin = 2
    if is_in_period(hjqyExchangeBUFFTime) and attack_type == 2:
        need_hjqy_coin = need_hjqy_coin * hjqyItemRate

    if need_hjqy_coin > player.finance[const.HJQYCOIN]:
        logger.error("hjqy coin not enough！")
        response.res.result = False
        response.res.result_no = 21031
        return response.SerializePartialToString()


    red_best_skill_id = request.skill
    _skill_id, red_best_skill_level = player.line_up_component.get_skill_info_by_unpar(red_best_skill_id)
    save_line_up_order(line_up, player, red_best_skill_id)

    player.fight_cache_component.stage_id = request.stage_id
    red_units = player.fight_cache_component.get_red_units()
    blue_units = remote_gate['world'].blue_units_remote(boss_id)
    seed1, seed2 = get_seeds()
    fight_result = remote_gate['world'].hjqy_battle_remote(boss_id, red_units, red_best_skill_id, red_best_skill_level, seed1, seed2)

    # 消耗讨伐令
    player.finance.consume(const.FIGHTTOKEN, need_hjqy_coin)

    response.fight_result = fight_result
    pvp_assemble_units(red_units, blue_units, response)
    response.red_best_skill= red_best_skill_id
    response.red_best_skill_level = red_best_skill_level
    response.seed1 = seed1
    response.seed2 = seed2
    response.attack_type = attack_type
    response.res.result = True
    return response.SerializePartialToString()



@remoteserviceHandle('gate')
def add_reward_2104(pro_data, player):
    """
    获取累积奖励
    request:HjqyAddRewardRequest
    response:HjqyAddRewardResponse
    """
    # 检查是否可领取
    request = hjqy_pb2.HjqyAddRewardRequest()
    request.ParseFromString(pro_data)
    response = hjqy_pb2.HjqyAddRewardResponse()

    damage_hp = remote_gate['world'].hjqy_damage_hp_remote(player.base_info.id)
    hjqy_info = game_configs.hjqy_config.get(request.id)

    if hjqy_info.output_requirements > damage_hp:
        logger.debug("damage_hp is not enough!")
        response.res.result = False
        response.res.result_no = 21041
        return response.SerializePartialToString()

    # 检查奖励是否被领取
    if request.id in player.hjqy_component.received_ids:
        logger.debug("has got the reward!")
        response.res.result = False
        response.res.result_no = 21042
        return response.SerializePartialToString()

    # 掉落
    data = gain(player, hjqy_info.get("rewards"), const.HJQY_ADD_REWARD)
    get_return(player, data, response.gain)

    # 保存已经获取的id
    player.hjqy_component.received_ids.append(request.id)
    player.hjqy_component.save_data()
    response.res.result = True
    return response.SerializePartialToString()


