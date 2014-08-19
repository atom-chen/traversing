# -*- coding:utf-8 -*-
"""
created by server on 14-8-13下午3:32.
"""
from app.game.component.baseInfo.slot_base_info import SlotBaseInfoComponent


class HeroSlotComponent(SlotBaseInfoComponent):
    """阵容英雄格子
    """

    def __init__(self, owner, slot_no, activation=False, hero_no=0, base_name=''):
        super(HeroSlotComponent, self).__init__(owner, slot_no, base_name, activation)

        self._hero_no = hero_no  # 英雄

    @property
    def hero_no(self):
        """英雄编号
        """
        return self._hero_no

    @hero_no.setter
    def hero_no(self, hero_no):
        self._hero_no = hero_no

    @property
    def hero_obj(self):
        """取得英雄对象
        """
        return self.owner.get_hero_obj(self._hero_no) if self._hero_no else None

    @property
    def link(self):
        """羁绊
        """
        link_data = {}
        for i in range(1, 6):
            link_no = getattr(self.hero_obj.hero_links, 'link%s' % i)  # 羁绊技能
            trigger_list = getattr(self.hero_obj.hero_links, 'trigger%s' % i)  # 羁绊触发条件
            if not link_no:
                continue

            result = self.__is_activation(trigger_list)
            link_data[link_no] = result

        return link_data

    def __is_activation(self, trigger_list):
        """羁绊是否激活
        @param trigger_list: 羁绊触发条件列表
        @return:
        """
        if not trigger_list:
            return 0
        activation = 1
        equipment_ids = self.owner.equipment_nos  # 装备编号
        for no in trigger_list:
            if len('%s' % no) == 5:  # 英雄ID
                if no not in self.owner.hero_nos:  # 羁绊需要英雄不在阵容中
                    activation = 0
                    break
            elif len('%s' % no) == 6:  # 装备ID
                if no not in equipment_ids:  # 羁绊需要的装备不在阵容中
                    activation = 0
                    break
        return activation
