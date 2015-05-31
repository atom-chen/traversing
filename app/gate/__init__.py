#coding:utf8

import action
from gfirefly.server.logobj import logger
from app.gate.core.users_manager import UsersManager
from gtwisted.core import reactor
from gfirefly.server.globalobject import GlobalObject
from shared.utils.ranking import Ranking
from shared.tlog import tlog_action
from app.gate.redis_mode import tb_character_info
from shared.utils.const import const
import time


front_ip = GlobalObject().json_config['front_ip']
front_port = GlobalObject().json_config['front_port']
name = GlobalObject().json_config['name']
server_no = GlobalObject().allconfig['server_no']


def tick():
    result = GlobalObject().remote['login'].server_sync_remote(name, front_ip,
                                                               front_port,
                                                               '1',
                                                               server_no)
    if result is False:
        reactor.callLater(1, tick)
    else:
        reactor.callLater(60, tick)
    logger.info('server online num:%s', UsersManager().get_online_num())
    tlog_action.log('OnlineNum', UsersManager().get_online_num())

reactor.callLater(1, tick)
