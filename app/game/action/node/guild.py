# -*- coding:utf-8 -*-
"""
created by server on 14-7-17下午4:50.
"""
from app.game.service.gatenoteservice import remote_service_handle
from app.game.logic.guild import *


@remote_service_handle
def create_guild_801(dynamic_id, pro_data):
    """创建公会
    """
    print('cuick,AAAAAAAAAAAAAAAAA,01,node,create_guild_801')
    return create_guild(dynamic_id, pro_data)


@remote_service_handle
def join_guild_802(dynamic_id, pro_data):
    """加入公会
    """
    print('cuick,BBBBBBBBBBBBBBBBBB,01,node,join_guild_802')
    return join_guild(dynamic_id, pro_data)


@remote_service_handle
def exit_guild_803(dynamic_id, pro_data):
    """退出公会
    """
    print('cuick,CCCCCCCCCCCCCCCCCC,01,node,exit_guild_803')
    return exit_guild(dynamic_id, pro_data)


@remote_service_handle
def editor_call_804(dynamic_id, pro_data):
    """编辑公告
    """
    print('cuick,DDDDDDDDDDDDDDDDDDD,01,node,editor_call_804')
    return editor_call(dynamic_id, pro_data)


@remote_service_handle
def deal_apply_805(dynamic_id, pro_data):
    """处理加入公会申请
    """
    print('cuick,EEEEEEEEEEEEEEEEEEE,01,node,exit_guild_805')
    return deal_apply(dynamic_id, pro_data)


@remote_service_handle
def change_president_806(dynamic_id, pro_data):
    """
    """
    print('cuick,FFFFFFFFFFFFFFFFFFFFF,01,node,change_president_806')
    return change_president(dynamic_id, pro_data)


@remote_service_handle
def kick_807(dynamic_id, pro_data):
    """
    """
    print('cuick,GGGGGGGGGGGGGGGGGGGGGG,01,node,change_president_806')
    return kick(dynamic_id, pro_data)


@remote_service_handle
def promotion_808(dynamic_id, pro_data):
    """
    """
    print('cuick,HHHHHHHHHHHHHHHHHHHHHH,01,node,change_president_806')
    return promotion(dynamic_id, pro_data)


@remote_service_handle
def worship_809(dynamic_id, pro_data):
    """
    """
    print('cuick,HHHHHHHHHHHHHHHHHHHHHH,01,node,change_president_806')
    return worship(dynamic_id, pro_data)