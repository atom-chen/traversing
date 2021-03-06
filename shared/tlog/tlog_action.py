# coding: utf-8

from shared.tlog import log4tx
from shared.utils import xtime
# from utils.log import log_except
from gfirefly.server.logobj import logger
from gfirefly.server.globalobject import GlobalObject
import time

game_server_id = GlobalObject().allconfig['server_no']
game_app_id = GlobalObject().allconfig['msdk']['appid']
plat_id = 1


def player_register(player_data, handler, ip):
    log4tx.player_register(GameSvrId=game_server_id,
                           dtEventTime=xtime.strdatetime(),
                           GameAppID=game_app_id, PlatID=plat_id,
                           OpenID=player_data.id,
                           ClientVersion=handler.client_version,
                           SystemSoftware=handler.system_software,
                           SystemHardware=handler.system_hardware,
                           TelecomOper=handler.telecom_oper,
                           Network=handler.network,
                           ScreenWidth=handler.screen_width,
                           ScreenHight=handler.screen_hight,
                           Density=handler.density,
                           RegChannel=handler.login_channel,
                           UUID=handler.mac,
                           CpuHardware=handler.cpu_hardware,
                           Memory=handler.memory,
                           GLRender=handler.gl_render,
                           GLVersion=handler.gl_version,
                           DeviceId=handler.device_id, Nickname='nickname',
                           IP=ip)


def player_login(player_data, handler, ip):
    log4tx.player_login(GameSvrId=game_server_id,
                        dtEventTime=xtime.strdatetime(),
                        GameAppID=game_app_id,
                        PlatID=plat_id, Level=player_data.level,
                        PlayerFriendsNum=1,
                        ClientVersion=handler.client_version,
                        SystemSoftware=handler.system_software,
                        SystemHardware=handler.system_hardware,
                        TelecomOper=handler.telecom_oper,
                        Network=handler.network,
                        ScreenWidth=handler.screen_width,
                        ScreenHight=handler.screen_hight,
                        Density=handler.density,
                        LoginChannel=handler.login_channel, UUID=handler.mac,
                        CpuHardware=handler.cpu_hardware,
                        Memory=handler.memory, GLRender=handler.gl_render,
                        GLVersion=handler.gl_version,
                        DeviceId=handler.device_id, OpenID=player_data.id,
                        IP=ip)


def player_logout(player_data):
    online_time = int(time.time())-player_data.base_info.login_time
    log4tx.player_logout(GameSvrId=game_server_id,
                         dtEventTime=xtime.strdatetime(),
                         GameAppID=game_app_id,
                         PlatID=plat_id, Level=player_data.base_info.level,
                         OpenID=player_data.base_info.id,
                         OnlineTime=online_time)


def item_flow(player_data, addorreduce, itemtype, itemnum, itemid, itid,
              reason, after_num, event_id):
    log4tx.item_flow(PlatID=plat_id, GameSvrId=game_server_id,
                     dtEventTime=xtime.strdatetime(), GameAppID=game_app_id,
                     OpenID=player_data.base_info.id, ItemID=itemid,
                     ItemType=itemtype, AfterCount=after_num, Count=itemnum,
                     AddOrReduce=addorreduce, Reason=reason, Itid=itid,
                     ReasonEventID=event_id)


def player_exp_flow(player_data, beforelevel, gain_exp, reason):

    log4tx.player_exp_flow(GameSvrId=game_server_id,
                           dtEventTime=xtime.strdatetime(),
                           GameAppID=game_app_id,
                           OpenID=player_data.base_info.id,
                           PlatID=plat_id, ExpChange=gain_exp,
                           BeforeLevel=beforelevel,
                           AfterLevel=player_data.base_info.level,
                           Time=player_data.base_info.upgrade_time,
                           Reason=reason, Exp=player_data.base_info.exp)


def line_up_change(player_data, slot, hero_id, after_hero_id,
                   change_type):

    log4tx.line_up_change(GameSvrId=game_server_id,
                          dtEventTime=xtime.strdatetime(),
                          GameAppID=game_app_id,
                          OpenID=player_data.base_info.id,
                          PlatID=plat_id,
                          Slot=slot,
                          HeroId=hero_id,
                          AfterHeroId=after_hero_id,
                          ChangeType=change_type)


def hero_sacrifice(player_data, hero_id):

    log4tx.hero_sacrifice(GameSvrId=game_server_id,
                          dtEventTime=xtime.strdatetime(),
                          GameAppID=game_app_id,
                          OpenID=player_data.base_info.id,
                          PlatID=plat_id,
                          HeroId=hero_id)


def hero_break(player_data, hero_id, level):

    log4tx.hero_break(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,
                      HeroId=hero_id,
                      Level=level)


def inherit(player_data, inherit_type, origin_id, origin_item_id,
            target_id, target_item_id):

    log4tx.inherit(GameSvrId=game_server_id,
                   dtEventTime=xtime.strdatetime(),
                   GameAppID=game_app_id,
                   OpenID=player_data.base_info.id,
                   PlatID=plat_id,
                   OriginId=origin_id,
                   OriginItemId=origin_item_id,
                   TargetId=target_id,
                   TargetItemId=target_item_id,
                   InheritType=inherit_type)


def stage_flow(player_data, stage_id, result):

    log4tx.stage_flow(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,
                      StageId=stage_id,
                      Result=result)


def sweep_flow(player_data, stage_id, times, reason_event_id):

    log4tx.sweep_flow(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,
                      StageId=stage_id,
                      Times=times,
                      ReasonEventID=reason_event_id)


def creat_guild(player_data, guild_id, user_level):

    log4tx.creat_guild(GameSvrId=game_server_id,
                       dtEventTime=xtime.strdatetime(),
                       GameAppID=game_app_id,
                       OpenID=player_data.base_info.id,
                       PlatID=plat_id,
                       GuildId=guild_id,
                       UserLevel=user_level)


def deal_join_guild(player_data, guild_id, behandler, res_type):

    log4tx.deal_join_guild(GameSvrId=game_server_id,
                           dtEventTime=xtime.strdatetime(),
                           GameAppID=game_app_id,
                           OpenID=player_data.base_info.id,
                           PlatID=plat_id,
                           GuildId=guild_id,
                           BeHandler=behandler,
                           ResType=res_type)


def exit_guild(player_data, guild_id):

    log4tx.exit_guild(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,
                      GuildId=guild_id)


def guild_change_president(player_data, guild_id, target_id):

    log4tx.guild_change_president(GameSvrId=game_server_id,
                                  dtEventTime=xtime.strdatetime(),
                                  GameAppID=game_app_id,
                                  OpenID=player_data.base_info.id,
                                  PlatID=plat_id,
                                  GuildId=guild_id,
                                  TargetId=target_id)


def guild_kick(player_data, guild_id, target_id):

    log4tx.guild_kick(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,
                      GuildId=guild_id,
                      TargetId=target_id)


def guild_promotion(player_data, guild_id, be_id):

    log4tx.guild_promotion(GameSvrId=game_server_id,
                           dtEventTime=xtime.strdatetime(),
                           GameAppID=game_app_id,
                           OpenID=player_data.base_info.id,
                           PlatID=plat_id,
                           GuildId=guild_id,
                           BeId=be_id)


def guild_worship(player_data, guild_id, worship_type):

    log4tx.guild_worship(GameSvrId=game_server_id,
                         dtEventTime=xtime.strdatetime(),
                         GameAppID=game_app_id,
                         OpenID=player_data.base_info.id,
                         PlatID=plat_id,
                         GuildId=guild_id,
                         WorshipType=worship_type)


def travel_settle(player_data, stage, event_id, parameter, res,
                  is_fast_settle):

    log4tx.travel_settle(GameSvrId=game_server_id,
                         dtEventTime=xtime.strdatetime(),
                         GameAppID=game_app_id,
                         OpenID=player_data.base_info.id,
                         PlatID=plat_id,
                         Stage=stage,
                         EventId=event_id,
                         Parameter=parameter,
                         Res=res,
                         IsFastSettle=is_fast_settle)


def auto_travel(player_data, stage, time):

    log4tx.auto_travel(GameSvrId=game_server_id,
                       dtEventTime=xtime.strdatetime(),
                       GameAppID=game_app_id,
                       OpenID=player_data.base_info.id,
                       PlatID=plat_id,
                       Stage=stage,
                       Time=time)


def hero_refine(player_data, hero_id, refine):

    log4tx.hero_refine(GameSvrId=game_server_id,
                       dtEventTime=xtime.strdatetime(),
                       GameAppID=game_app_id,
                       OpenID=player_data.base_info.id,
                       PlatID=plat_id,
                       Refine=refine,
                       HeroId=hero_id)


def hero_upgrade(player_data, hero_id, change_level, level):

    log4tx.hero_upgrade(GameSvrId=game_server_id,
                        dtEventTime=xtime.strdatetime(),
                        GameAppID=game_app_id,
                        OpenID=player_data.base_info.id,
                        PlatID=plat_id,
                        Level=level,
                        ChangeLevel=change_level,
                        HeroId=hero_id)


def recharge(player_data, isfirst, recharege_id):

    log4tx.recharge(GameSvrId=game_server_id,
                    dtEventTime=xtime.strdatetime(),
                    GameAppID=game_app_id,
                    OpenID=player_data.base_info.id,
                    PlatID=plat_id,
                    Isfirst=isfirst,
                    RechargeId=recharege_id)


def round_flow(player_data, battle_id, battle_type, is_quick, result):

    log4tx.round_flow(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,

                      BattleID=battle_id,
                      BattleType=battle_type,
                      isQuick=is_quick,
                      Result=result)


def new_guide(player_data, sequence, my_sequence):

    log4tx.new_guide(GameSvrId=game_server_id,
                     dtEventTime=xtime.strdatetime(),
                     GameAppID=game_app_id,
                     OpenID=player_data.base_info.id,
                     PlatID=plat_id,

                     Sequence=sequence,
                     MySequence=my_sequence)


def online_num(num):

    log4tx.online_num(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,

                      Num=num)


def money_flow(player_data, after_money, money, reason, addorreduce,
               money_type):

    log4tx.money_flow(GameSvrId=game_server_id,
                      dtEventTime=xtime.strdatetime(),
                      GameAppID=game_app_id,
                      OpenID=player_data.base_info.id,
                      PlatID=plat_id,

                      Level=player_data.base_info.level,
                      AfterMoney=after_money,
                      Money=money, Reason=reason,
                      AddOrReduce=addorreduce,
                      MoneyType=money_type)


def item_money_flow(player_data, item_type, item_id, count, money,
                    money_type, discount_money, discount_money_type,
                    limit_vip_everyday, limit_vip, is_discount):

    log4tx.item_money_flow(GameSvrId=game_server_id,
                           dtEventTime=xtime.strdatetime(),
                           GameAppID=game_app_id,
                           OpenID=player_data.base_info.id,
                           PlatID=plat_id,

                           ItemType=item_type,
                           ItemID=item_id,
                           Count=count,
                           Money=money,
                           Level=player_data.base_info.level,
                           MoneyType=money_type,
                           DiscountMoney=discount_money,
                           DiscountMoneyType=discount_money_type,
                           LimitVipEveryday=limit_vip_everyday,
                           LimitVip=limit_vip,
                           IsDiscount=is_discount)


def equipment_enhance(player_data, equipmeng_no, equipmeng_id,
                      beforelevel, afterlevel):

    log4tx.equipment_enhance(GameSvrId=game_server_id,
                             dtEventTime=xtime.strdatetime(),
                             GameAppID=game_app_id,
                             OpenID=player_data.base_info.id,
                             PlatID=plat_id,

                             EquipmentNo=equipmeng_no,
                             EquipmentId=equipmeng_id,
                             BeforeLevel=beforelevel,
                             AfterLevel=afterlevel)


def equipment_compose(player_data, equipmeng_no, equipmeng_id):

    log4tx.equipment_compose(GameSvrId=game_server_id,
                             dtEventTime=xtime.strdatetime(),
                             GameAppID=game_app_id,
                             OpenID=player_data.base_info.id,
                             PlatID=plat_id,

                             EquipmentNo=equipmeng_no,
                             EquipmentId=equipmeng_id)


def equipment_melting(player_data, equipmeng_no, equipmeng_id):

    log4tx.equipment_melting(GameSvrId=game_server_id,
                             dtEventTime=xtime.strdatetime(),
                             GameAppID=game_app_id,
                             OpenID=player_data.base_info.id,
                             PlatID=plat_id,

                             EquipmentNo=equipmeng_no,
                             EquipmentId=equipmeng_id)


# TLOG分类打印函数
tlog_funcs = {}
tlog_funcs['PlayerLogin'] = player_login
tlog_funcs['PlayerLogout'] = player_logout
tlog_funcs['PlayerRegister'] = player_register
tlog_funcs['ItemFlow'] = item_flow
tlog_funcs['PlayerExpFlow'] = player_exp_flow
tlog_funcs['LineUpChange'] = line_up_change
tlog_funcs['HeroBreak'] = hero_break
tlog_funcs['Inherit'] = inherit
tlog_funcs['StageFlow'] = stage_flow
tlog_funcs['SweepFlow'] = sweep_flow
tlog_funcs['CreatGuild'] = creat_guild
tlog_funcs['DealJoinGuild'] = deal_join_guild
tlog_funcs['ExitGuild'] = exit_guild
tlog_funcs['GuildChangePresident'] = guild_change_president
tlog_funcs['GuildKick'] = guild_kick
tlog_funcs['GuildPromotion'] = guild_promotion
tlog_funcs['GuildWorship'] = guild_worship
tlog_funcs['TravelSettle'] = travel_settle
tlog_funcs['AutoTravel'] = auto_travel
tlog_funcs['HeroRefine'] = hero_refine
tlog_funcs['HeroUpgrade'] = hero_upgrade
tlog_funcs['Recharge'] = recharge
tlog_funcs['RoundFlow'] = round_flow
tlog_funcs['NewGuide'] = new_guide
tlog_funcs['OnlineNum'] = online_num
tlog_funcs['MoneyFlow'] = money_flow
tlog_funcs['ItemMoneyFlow'] = item_money_flow
tlog_funcs['HeroSacrifice'] = hero_sacrifice
tlog_funcs['EquipmentEnhance'] = equipment_enhance
tlog_funcs['EquipmentCompose'] = equipment_compose
tlog_funcs['EquipmentMelting'] = equipment_melting


def log(mod, *args, **kwds):
    """
    打印TLOG
    """
    # try:
    tlog_funcs[mod](*args, **kwds)
    # except:
    #     pass
    #     log_except(mod)
