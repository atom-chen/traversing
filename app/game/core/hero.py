# -*- coding:utf-8 -*-
"""
created by server on 14-6-25下午5:27.
"""

from shared.db_opear.configs_data.game_configs import hero_config, hero_exp_config
from gtwisted.utils import log
import cPickle

class Hero(object):
    """武将类"""

    def __init__(self, mmode=None):
        """
        :param mmode: 对应redis中的一条数据
        :field _level: 等级
        :field _break_level: 突破等级
        :field _exp: 当前等级的经验
        :field _equipmentids: 装备IDs
        """

        self._hero_id = ''
        self._hero_no = 0
        self._level = 0
        self._exp = 0
        self._break_level = 0
        self._equipment_ids = []
        self._mmode = mmode
        self._config = None

    def init_data(self):
        if not self._mmode:
            log.msg("mmode=None 武将初始化数据为空！")
            return
        data = self._mmode.get('data')
        print "武将初始化nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn"
        print "level", data.get("level")
        print "exp", data.get('exp')
        print "no", data.get("hero_no")
        print data.get("break_level")
        print data.get("equipment_ids")
        self._hero_id = data.get("id")
        self._hero_no = data.get("hero_no")
        self._level = data.get("level")
        self._exp = data.get("exp")
        self._break_level = data.get("break_level")
        self._equipment_ids = data.get("equipment_ids")  # 穿戴装备列表
        _config = hero_config.get(self._hero_no)
        if not _config:
            log.msg("武将%s配置文件初始化失败！" % self._hero_no)
        # print "@", hero_config
        self._config = _config

    @property
    def hero_no(self):
        return self._hero_no

    @hero_no.setter
    def hero_no(self, value):
        self._hero_no = value
        self.save_data()

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, value):
        self._level = value
        self.save_data()

    @property
    def exp(self):
        return self._exp

    @exp.setter
    def exp(self, value):
        self._exp = value
        self.save_data()

    @property
    def break_level(self):
        return self._break_level

    @break_level.setter
    def break_level(self, value):
        self._break_level = value
        self.save_data()

    @property
    def equipment_ids(self):
        return self._equipment_ids

    @equipment_ids.setter
    def equipment_ids(self, value):
        self._equipment_ids = value
        self.save_data()

    @property
    def config(self):
        return self._config

    @property
    def mmode(self):
        return self._mmode

    @mmode.setter
    def mmode(self, value):
        self._mmode = value

    def get_all_exp(self):
        """根据等级+当前等级经验，得到总经验"""
        total_exp = 0
        for level in range(1, self._level):
            total_exp += hero_exp_config[level].get('exp', 0)

        return total_exp + self._exp

    def upgrade(self, exp):
        """根据经验升级"""
        level = self._level
        temp_exp = self._exp
        temp_exp += exp
        while True:
            current_level_exp = hero_exp_config[level].get('exp', 0)
            if current_level_exp < temp_exp:
                level += 1
                temp_exp -= current_level_exp
            else:
                break

        self.level = level
        self.exp = temp_exp
        return level, temp_exp

    def save_data(self):
        hero_property = {
            'hero_no': self._hero_no,
            'level': self._level,
            'exp': self._exp,
            'break_level': self._break_level,
            'equipment_ids': cPickle.dumps(self._equipment_ids)
        }
        self._mmode.update('property', hero_property)

































