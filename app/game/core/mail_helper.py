# -*- coding:utf-8 -*-
from app.proto_file.db_pb2 import Mail_PB
import time
from app.game.action.root import netforwarding
from gfirefly.server.logobj import logger


def send_mail(conf_id=0, nickname='', receive_id=0, guild_name='',
              guild_p_num=0, guild_level=0, guild_id=0, pvp_rank=0,
              rune_num=0):
    mail = Mail_PB()
    if conf_id:
        mail.config_id = conf_id
    if nickname:
        mail.nickname = nickname
    if guild_name:
        mail.guild_name = guild_name
    if guild_p_num:
        mail.guild_person_num = guild_p_num
    if guild_level:
        mail.guild_level = guild_level
    if guild_id:
        mail.guild_id = guild_id
    if pvp_rank:
        mail.pvp_rank = pvp_rank
    if rune_num:
        mail.rune_num = rune_num
    mail.send_time = int(time.time())
    mail_data = mail.SerializePartialToString()
    if not netforwarding.push_message('receive_mail_remote',
                                      receive_id, mail_data):
        logger.error('guild appoint mail push message fail')
