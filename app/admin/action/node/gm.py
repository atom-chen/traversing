# -*- coding:utf-8 -*-
"""
created by sphinx on
"""
import json
from gfirefly.server.globalobject import webserviceHandle
from flask import request
from gfirefly.server.logobj import logger
from gfirefly.server.globalobject import GlobalObject
import cPickle
import urllib
import re
import os
import time
from app.proto_file.db_pb2 import Mail_PB
from app.admin.redis_mode import tb_guild_info, tb_guild_name, \
    tb_character_info
from app.admin.action.root.netforwarding import push_message
from app.proto_file.db_pb2 import Stamina_DB
from shared.utils import trie_tree


remote_gate = GlobalObject().remote['gate']
MASTER_WEBPORT = GlobalObject().allconfig['master']['webport']


@webserviceHandle('/gmtestdata:name')
def gm_add_test_data(account_name='hello world'):
    # account_name = request.args.get('name')
    return account_name


@webserviceHandle('/gm', methods=['post', 'get'])
def gm():
    response = {}
    res = {}
    admin_command = ['update_excel', 'get_user_info', 'send_mail',
                     'get_user_hero_chips', 'get_user_eq_chips',
                     'get_user_finances', 'get_user_items',
                     'get_user_guild_info']
    if request.args:
        t_dict = request.args
    else:
        t_dict = request.form

    logger.info('gm2admin,command:%s', t_dict['command'])

    if t_dict['command'] in admin_command:
        com = t_dict['command'] + "(t_dict)"
        res = eval(com)
    else:
        res = remote_gate.from_admin_rpc_remote(cPickle.dumps(t_dict))
        if res['success'] == 2:
            com = t_dict['command'] + "(t_dict)"
            res = eval(com)
    logger.info('######################################erver2gm:%s', res)

    return json.dumps(res)


def update_excel(args):
    url = args['excel_url']
    urllib.urlretrieve(url, 'config/excel_cpickle')
    com = "curl localhost:%s/reloadmodule" % MASTER_WEBPORT
    os.system(com)
    return {"success": 1}


def get_user_info(args):
    print args
    if args['search_type'] == '1':
        character_obj = tb_character_info.getObj(args['search_value'])
        isexist = character_obj.exists()
    elif args['search_type'] == '2':
        nickname_obj = tb_character_info.getObj('nickname')
        isexist = nickname_obj.hexists(args['search_value'])
        pid = nickname_obj.hget(args['search_value'])
        character_obj = tb_character_info.getObj(pid)
    else:
        return {'success': 0, 'message': 1}

    if not isexist:
        return {'success': 0, 'message': 2}

    character_info = character_obj.hmget(['nickname', 'attackpoint',
                                          'heads', 'upgrade_time',
                                          'level', 'id', 'exp',
                                          'vip_level', 'register_time',
                                          'upgrade_time', 'guild_id',
                                          'position'])
    if character_info['guild_id'] == 'no':
        position = 0
        guild_name = ''
        guild_id = ''
    else:
        guild_id = character_info['guild_id']
        guild_obj = tb_guild_info.getObj()
        if guild_obj.exists():
            guild_info = guild_obj.hmget(['name'])
            positon = character_info['positon']
            guild_name = guild_info['name']
        else:
            position = 0
            guild_name = ''

    return {'success': 1,
            'message': {'uid': character_info['id'],
                        'nickname': character_info['nickname'],
                        'level': character_info['level'],
                        'exp': character_info['exp'],
                        'vip_level': character_info['vip_level'],
                        'register_time': character_info['register_time'],
                        'recently_login_time': character_info['upgrade_time'],
                        'guild_id': guild_id,
                        'guild_name': guild_name,
                        'position': position}}


def send_mail(args):
    mail = Mail_PB()
    # mail.sender_id = player.base_info.id
    mail.sender_name = args['sender_name']
    mail.sender_icon = int(args['sender_icon'])
    mail.receive_name = ''
    mail.title = args['title']
    mail.content = args['text']
    mail.mail_type = 2
    mail.prize = ''
    mail.send_time = int(time.time())
    # mail_data = mail.SerializePartialToString()

    if args['uids'] == '0':
        users = tb_character_info.smem('all')
        print users
        for uid in users:
            mail.receive_id = uid
            push_message('receive_mail_remote', uid,
                         mail.SerializeToString())
    else:
        for uid in args['uids'].split(';'):
            mail.receive_id = int(uid)
            mail_data = mail.SerializeToString()
            push_message('receive_mail_remote', int(uid),
                         mail.SerializeToString())
    return {'success': 1}


def modify_user_info(args):
    # oldvcharacter = VCharacterManager().get_by_id(int(args.get('uid')))
    # if oldvcharacter:
    #     args = (args.get('command'), oldvcharacter.dynamic_id,
    #             cPickle.dumps(args))
    #     child_node = groot.child(oldvcharacter.node)
    #     return child_node.callbackChild(*args)
    # else:
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}

    if args['attr_name'] == 'user_level':
        data = {'level': int(args['attr_value'])}
        character_obj.hmset(data)
        return {'success': 1}
    elif args['attr_name'] == 'vip_level':
        data = {'vip_level': int(args['attr_value'])}
        character_obj.hmset(data)
        return {'success': 1}
    elif args['attr_name'] == 'user_exp':
        data = {'exp': int(args['attr_value'])}
        character_obj.hmset(data)
        return {'success': 1}
    elif args['attr_name'] == 'buy_stamina_times':
        stamina_data = character_obj.hget('stamina')
        stamina = Stamina_DB()
        stamina.ParseFromString(stamina_data)
        stamina.buy_stamina_times = int(args['attr_value'])
        data = {'stamina': stamina.SerializeToString()}
        character_obj.hmset(data)
        return {'success': 1}
    elif args['attr_name'] == 'stamina':
        finance = character_obj.hget('finances')
        finance[7] = int(args['attr_value'])
        data = {'finances': finance}
        character_obj.hmset(data)
        return {'success': 1}
    elif args['attr_name'] == 'nickname':
        nickname = args['attr_value']
        match = re.search(u'[\uD800-\uDBFF][\uDC00-\uDFFF]', nickname)
        if match:
            return {'success': 0, 'message': 2}

        if trie_tree.check.replace_bad_word(nickname) != nickname:
            return {'success': 0, 'message': 2}

        nickname_obj = tb_character_info.getObj('nickname')
        result = nickname_obj.hsetnx(args['attr_value'], args['uid'])
        if result:
            data = {'nickname': args['attr_value']}
            character_obj.hmset(data)
            return {'success': 1}
        else:
            return {'success': 0, 'message': 0}
    else:
        return {'success': 0, 'message': 3}


def get_user_hero_chips(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}

    hero_chips_data = character_obj.hget('hero_chips')
    message = {}
    if hero_chips_data:
        for no, num in hero_chips_data.items():
            message[no] = num

    return {'success': 1, 'message': message}


def get_user_eq_chips(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}

    equipment_chips = character_obj.hget('equipment_chips')
    message = {}
    if equipment_chips:
        for no, num in equipment_chips.items():
            message[no] = num

    return {'success': 1, 'message': message}


def get_user_items(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}

    items = character_obj.hget('items')
    message = {}
    if items:
        for no, num in items.items():
            message[no] = num

    return {'success': 1, 'message': message}


def get_user_finances(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}

    finances = character_obj.hget('finances')
    del finances[0]

    return {'success': 1, 'message': finances}


def get_user_guild_info(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}

    guild_id = character_obj.hget('guild_id')
    if guild_id == 'no':
        return {'success': 0, 'message': 2}

    message = {}
    position = character_obj.hget('position')
    contribution = character_obj.hget('contribution')
    all_contribution = character_obj.hget('all_contribution')
    k_num = character_obj.hget('k_num')
    worship = character_obj.hget('worship')
    worship_time = character_obj.hget('worship_time')
    exit_time = character_obj.hget('exit_time')
    message = {'guild_id': guild_id,
               'position': position,
               'contribution': contribution,
               'all_contribution': all_contribution,
               'k_num': k_num,
               'worship': worship,
               'worship_time': worship_time,
               'exit_time': exit_time}

    return {'success': 1, 'message': message}


def ban_user(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}
    closure = character_obj.hget('closure')
    data = {'closure': int(args['attr_value'])}
    character_obj.hmset(data)
    return {'success': 1}


def ban_speak(args):
    character_obj = tb_character_info.getObj(int(args.get('uid')))
    if not character_obj.exists():
        return {'success': 0, 'message': 1}
    closure = character_obj.hget('gag')
    data = {'gag': int(args['attr_value'])}
    character_obj.hmset(data)
    return {'success': 1}
