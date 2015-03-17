# -*- coding:utf-8 -*-
"""
created by server on 14-6-27下午6:49.
"""
from shared.db_opear.configs_data import game_configs
from app.game.component.Component import Component
from app.game.redis_mode import tb_character_info
from gfirefly.server.logobj import logger
from shared.utils.const import const
from gfirefly.server.globalobject import GlobalObject


# const.COIN = 1
# const.GOLD = 2
# const.HERO_SOUL = 3
# const.JUNIOR_STONE = 4
# const.MIDDLE_STONE = 5
# const.HIGH_STONE = 6
# const.STAMINA = 7
# const.PVP = 8
# const.GUILD = 9
# const.GUILD2 = 11
# const.TEAM_EXPERIENCE = 12
# const.NECTAR = 13
# const.STONE1 = 14
# const.STONE2 = 15
# const.EQUIPMENT_ELITE = 21
# const.RESOURCE_MAX = 23

class CharacterFinanceComponent(Component):
    """货币"""

    def __init__(self, owner, coin=0, gold=0, hero_soul=0):
        super(CharacterFinanceComponent, self).__init__(owner)
        self._finances = [0] * const.RESOURCE_MAX

    def init_data(self, data):
        self._finances = data['finances']
        while len(self._finances) < const.RESOURCE_MAX:
            self._finances.append(0)

    def save_data(self):
        character_obj = tb_character_info.getObj(self.owner.base_info.id)
        character_obj.hset('finances', self._finances)

    def new_data(self):
        self._finances = [0] * const.RESOURCE_MAX
        for t, v in game_configs.base_config.get('resource_for_InitUser').items():
            self._finances[t] = v
        return {'finances': self._finances}

    def __getitem__(self, res_type):
        if res_type >= len(self._finances):
            logger.error('get error resource type:%s', res_type)
            return None
        return self._finances[res_type]

    def __setitem__(self, res_type, value):
        if res_type >= len(self._finances):
            logger.error('set error resource type:%s', res_type)
            return
        self._finances[res_type] = value

    @property
    def coin(self):
        return self._finances[const.COIN]

    @coin.setter
    def coin(self, coin):
        self._finances[const.COIN] = coin

    @property
    def hero_soul(self):
        return self._finances[const.HERO_SOUL]

    @hero_soul.setter
    def hero_soul(self, value):
        self._finances[const.HERO_SOUL] = value

    @property
    def gold(self):
        return self._finances[const.GOLD]

    @gold.setter
    def gold(self, gold):
        self._finances[const.GOLD] = gold

    @property
    def pvp_score(self):
        return self._finances[const.PVP]

    @pvp_score.setter
    def pvp_score(self, value):
        self._finances[const.PVP] = value

    def is_afford(self, fType, value):
        if fType >= len(self._finances):
            logger.error('afford error finance type:%s', fType)
            return False
        if self._finances[fType] < value:
            return False
        return True

    def consume(self, fType, num):
        if fType >= len(self._finances):
            logger.error('consume error finance type:%s', fType)
            return False
        if num > self._finances[fType]:
            logger.error('not enough finance:%s:%s:%s',
                         fType, self._finances[fType], num)
            return False
        if fType == 2:
            return self.consume_gold(num)
        else:
            self._finances[fType] -= num
        return True

    def add(self, fType, num):
        if fType >= len(self._finances):
            logger.error('consume error finance type:%s', fType)
            return False
        if fType == 2:
            self.add_gold(num)
        else:
            self._finances[fType] += num
        return True

    def add_coin(self, num):
        if const.PAY:
            GlobalObject().pay.present_m()
            coin = GlobalObject().pay.get_balance_m()
            self._finances[const.COIN] = coin
        self._finances[const.COIN] += num

    def consume_coin(self, num):
        if num < self._finances[const.COIN]:
            return False
        self._finances[const.COIN] -= num
        if const.PAY:
            pay = GlobalObject().pay
            pay.pay_m()
            gold = pay.get_balance_m()
            if gold != self._finances[const.COIN]:
                logger.error("gold num != tencent server num")
            self._finances[const.COIN] = gold
        return True

    def add_gold(self, num):
        self._finances[const.GOLD] += num

    def consume_gold(self, num):
        if num > self._finances[const.GOLD]:
            return False
        self._finances[const.GOLD] -= num
        return True

    def add_hero_soul(self, num):
        self._finances[const.HERO_SOUL] += num

    def consume_hero_soul(self, num):
        self._finances[const.HERO_SOUL] -= num
