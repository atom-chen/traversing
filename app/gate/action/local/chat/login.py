#-*- coding:utf-8 -*-
"""
created by server on 14-5-20下午12:11.
"""
from app.gate.service.local.gateservice import local_service_handle
from app.proto_file.chat import chat_pb2
from gfirefly.server.globalobject import GlobalObject


@local_service_handle
def login_chat_1001(command_id, dynamic_id, request_proto):
    """登录聊天服务器
    """
    argument = chat_pb2.LoginToChatRequest()
    argument.ParseFromString(request_proto)
    response = chat_pb2.ChatResponse()
    character_id = argument.owner.id
    character_nickname = argument.owner.nickname

    result = GlobalObject().root.callChild('chat', command_id, \
                                           character_id, dynamic_id, character_nickname)
    response.result = result
    return response.SerializeToString()


# @nodeservice_handle
# def logout_chat_1003(command_id, dynamic_id):
#     """登出聊天服务器
#     """
#     return localservice.callTarget(command_id, dynamic_id)
