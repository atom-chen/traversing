# -*- coding: utf-8 -*-
"""
created by wzp on 14-6-19下午7: 51.
"""
from app.game.service.gatenoteservice import remoteservice_handle
from app.game.core.character.PlayerCharacter import PlayerCharacter
from app.game.core.PlayersManager import PlayersManager



@remoteservice_handle
def enter_scene_601(dynamicid):
    """进入场景"""
    # if not player:
    #     player = PlayerCharacter(characterid, dynamic_id=dynamicid)
    # PlayersManager().addPlayer(player)
    # playerinfo = player.formatInfo()
    # responsedata = {'result': True, 'message': '',
    #                 'data': {'cid': playerinfo['id'],
    #                         'name': playerinfo['nickname'],
    #                         'level': playerinfo['level'],
    #                         'exp': playerinfo['exp'],
    #                         'maxexp': playerinfo['maxExp'],
    #                         'coin': playerinfo['coin'],
    #                         'yuanbao': playerinfo['gold'],
    #                         'power': playerinfo['maxHp'],
    #                         'gas': playerinfo['energy'],
    #                         'profession': playerinfo['profession']}
    #                 }
    #return responsedata
    return "I get to enter scene"