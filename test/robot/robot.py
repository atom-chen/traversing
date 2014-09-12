# -*- coding:utf-8 -*-
"""
created by server on 14-8-8下午2:45.
"""

from robotbase import RobotBase
from app.proto_file import account_pb2
from app.proto_file import player_request_pb2
from app.proto_file.common_pb2 import CommonResponse
from app.proto_file.game_pb2 import GameLoginResponse
from app.proto_file.player_request_pb2 import CreatePlayerRequest


class Robot(RobotBase):
    def __init__(self):
        self.id = 0
        self.nickname = ''

    def __init__(self, manager, user_name, pwd, nickname):
        RobotBase.__init__(self)

        self.on_connection_made = self.connection_made
        self.on_account_login_result = None
        self.on_character_login_result = None

        self._user_name = user_name  # 'test32'
        self._password = pwd  # '123456'
        self._nickname = nickname  # 'bab5'
        manager.register_robot(self)

    def connection_made(self):
        argument = account_pb2.AccountInfo()
        argument.user_name = self._user_name
        argument.password = self._password
        argument.type = 2
        self.send_message(argument, 1)

    def acount_register_1(self, message):
        argument = account_pb2.AccountResponse()
        argument.ParseFromString(message)
        # print 'account register', argument.result

        argument = account_pb2.AccountLoginRequest()
        argument.user_name = self._user_name
        argument.password = self._password
        argument.key.key = ''
        self.send_message(argument, 2)

    def account_login_2(self, message):
        response = account_pb2.AccountResponse()
        response.ParseFromString(message)
        print 'login request result:', response.result
        self.on_account_login_result(response.result)

        request = player_request_pb2.PlayerLoginRequest()
        request.token = 'ea93b955c76de71380559058cdcd6932'
        self.send_message(request, 4)

    def character_login_4(self, message):
        argument = GameLoginResponse()
        argument.ParseFromString(message)
        format_str = 'character login result:%s id:%d nickname:%s level;%s'
        print format_str % (argument.res.result,
                            argument.id,
                            argument.nickname,
                            argument.level)
        if not argument.res.result:
            self.on_character_login_result(argument.res.result)

        self.id = argument.id
        self.nickname = argument.nickname
        request = CreatePlayerRequest()
        request.nickname = self._nickname
        self.send_message(request, 5)

    def change_nickname_5(self, message):
        response = CommonResponse()
        response.ParseFromString(message)
        print 'change nickname result:', response.result
        self.on_character_login_result(True)
