# -*- coding:utf-8 -*-
"""
created by server on 14-7-7上午11:39.
"""
from app.game.component.Component import Component
from app.game.core.equipment.equipment import Equipment
from app.game.redis_mode import tb_character_equipments
from app.game.redis_mode import tb_equipment_info
from shared.utils.pyuuid import get_uuid


class CharacterEquipmentPackageComponent(Component):
    """角色的装备背包
    """
    def __init__(self, owner):
        super(CharacterEquipmentPackageComponent, self).__init__(owner)
        self._equipments = []  # 装备列表 [装备ID]
        self._equipments_obj = {}  # {装备ID：装备obj}

        # self._equipments_chip = {}  # 装备碎片 {装备No: 装备num}

    def init_data(self):
        equipments_data = tb_character_equipments.getObjData(self.owner.base_info.id)
        if equipments_data:
            print 'equipments_data:', equipments_data
            self._equipments = equipments_data.get('equipments')
            for equipment_id in self._equipments:
                equipment_data = tb_equipment_info.getObjData(equipment_id)
                equipment_info = equipment_data.get('equipment_info')
                print 'equipment_data:', equipment_data
                equipment_no = equipment_info.get('no')  # 装备编号
                strengthen_lv = equipment_info.get('slv')  # 装备强化等级
                awakening_lv = equipment_info.get('alv')  # 装备觉醒等级
                equipment_obj = Equipment(equipment_id, '', equipment_no, strengthen_lv, awakening_lv)
                self._equipments_obj[equipment_id] = equipment_obj
        else:
            tb_character_equipments.new({'id': self.owner.base_info.id, 'equipments': []})

        self.add_equipment(10001)

    def add_equipment(self, equipment_no):
        """添加装备
        """
        equipment_id = get_uuid()
        equipment_obj = Equipment(equipment_id, '', equipment_no)
        self._equipments.append(equipment_id)
        self._equipments_obj[equipment_id] = equipment_obj

        equipment_obj.save_data(self.owner.base_info.id)
        self.save_data()

    def save_data(self):
        equipments_obj = tb_character_equipments.getObj(self.owner.base_info.id)
        equipments_obj.update('equipments', self._equipments)














