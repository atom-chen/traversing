#!/usr/bin/env python
# -*- coding: utf-8 -*-
from shared.db_opear.configs_data import game_configs
from app.game.component.fight.stage_logic import stage_util, base_stage
from gfirefly.server.logobj import logger
import time
from shared.tlog import tlog_action
from app.game.core.task import hook_task, CONDITIONId


class ActStageLogic(base_stage.BaseStageLogic):
    """docstring for 活动关卡"""
    def __init__(self, player, stage_id):
        super(ActStageLogic, self).__init__(player, stage_id)

    def check(self):
        """校验关卡是否开启"""
        player = self._player
        conf = self.get_stage_config()
        tm_time = time.localtime(player.stage_component.act_stage_info[1])
        if tm_time.tm_yday == time.localtime().tm_yday \
            and game_configs.vip_config.get(player.base_info.vip_level).activityCopyTimes - player.stage_component.act_stage_info[0] < conf.timesExpend:
            logger.error("活动关卡开始战斗出错: %s" % 805)
            return {'result': False, 'result_no': 805}  # 805 次数不足
        if conf.weeklyControl:
            if time.localtime().tm_wday == 6:
                wday = 0
            else:
                wday = time.localtime().tm_wday + 1

            if not conf.weeklyControl[wday]:
                logger.error('week error,804:%s', time.localtime().tm_wday)
                return {'result': False, 'result_no': 804}  # 804 不在活动时间内

        # 时间限制
        open_time = time.mktime(time.strptime(conf.open_time, '%Y-%m-%d %H:%M'))
        close_time = time.mktime(time.strptime(conf.close_time, '%Y-%m-%d %H:%M'))
        if not open_time <= time.time() <= close_time:
            logger.error('time error,804,:%s', time.time())
            return {'result': False, 'result_no': 804}  # 804 不在活动时间内
        return {'result': True}

    def get_stage_config(self):
        """get_stage_config"""
        return stage_util.get_stage_config(game_configs.special_stage_config, "act_stages", self._stage_id)

    def settle(self, result, response):
        """docstring for 结算"""
        player = self._player
        conf = self.get_stage_config()
        stage_id = self._stage_id
        tm_time = time.localtime(player.stage_component.act_stage_info[1])
        if result:
            if tm_time.tm_yday == time.localtime().tm_yday:
                player.stage_component.act_stage_info[0] += conf.timesExpend
            else:
                player.stage_component.act_stage_info = [conf.timesExpend, int(time.time())]
            stage_util.settle(player, result, response, conf)
            hook_task(player, CONDITIONId.STAGE, stage_id)
            hook_task(player, CONDITIONId.ANY_ACT_STAGE, 1)
            tlog_action.log('RoundFlow', player, stage_id, 3, 0, 1)
        else:
            tlog_action.log('RoundFlow', player, stage_id, 3, 0, 0)
