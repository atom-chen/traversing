# -*- coding:utf-8 -*-
"""
created by server on 14-7-7下午5:26.
"""
from app.game.component.baseInfo.equipment_base_info import EquipmentBaseInfoComponent
from app.game.component.equipment.equipment_attribute import EquipmentAttributeComponent
from app.game.component.record.equipment_enhance import EquipmentEnhanceComponent
from app.game.redis_mode import tb_character_info
from shared.db_opear.configs_data import game_configs
from shared.db_opear.configs_data.common_item import CommonItem
from shared.utils.random_pick import random_pick_with_percent
from gfirefly.server.logobj import logger
# from shared.utils.const import const
import random
import copy


EQUIP_ATTR_CONFIG = game_configs.equipment_attribute_config


def init_equipment_attr(equipment_no, attr_id=0):
    mainAttr, minorAttr = {}, {}
    equipment_item = game_configs.equipment_config.get(equipment_no)
    if not equipment_item:
        logger.error('error equipment no:%s', equipment_no)
        return mainAttr, minorAttr

    equip_attr_id = equipment_item.attr if attr_id == 0 else attr_id
    logger.debug('init_equipment_attr %s %s', equip_attr_id, attr_id)
    equipment_attr_item = EQUIP_ATTR_CONFIG.get(int(equip_attr_id))
    if not equipment_attr_item:
        logger.error('error equipment attr no:%s:%s',
                     equip_attr_id, equipment_no)
        return mainAttr, minorAttr

    main_num = equipment_attr_item.get('mainAttrNum')
    minor_num_min, minor_num_min = equipment_attr_item.get('minorAttrNum')
    minor_num = random.randint(minor_num_min, minor_num_min)

    main_pool = copy.copy(equipment_attr_item.get('mainAttr'))
    minor_pool = copy.copy(equipment_attr_item.get('minorAttr'))

    for _ in range(main_num):
        at, avt, av, ai = rand_pick_attr(main_pool)
        mainAttr[at] = [avt, av, ai]
    for _ in range(minor_num):
        at, avt, av, ai = rand_pick_attr(minor_pool)
        minorAttr[at] = [avt, av, ai]

    assert main_num == len(mainAttr)
    assert minor_num == len(minorAttr)

    # calculation for prefx
    prefix = get_prefix(equipment_item, mainAttr, minorAttr)

    return mainAttr, minorAttr, prefix, equip_attr_id

def get_prefix(equipment_item, mainAttr, minorAttr):
    """docstring for get_prefix"""
    quality = equipment_item.get("quality")
    for item in game_configs.base_config.get("equPrefix")[quality]:
        ran = get_equip_rate(equipment_item, mainAttr, minorAttr)
        logger.debug("ran=========:%s" % ran)
        if item[0] <= ran and item[1] > ran:
            return item[2]
    return 0

def get_equip_rate(equipment_item, mainAttr, minorAttr):
    """当前装备/极限装备战斗力"""

    equip_attr_id = equipment_item.attr
    equipment_attr_item = EQUIP_ATTR_CONFIG.get(int(equip_attr_id))
    main_pool = copy.copy(equipment_attr_item.get('mainAttr'))
    minor_pool = copy.copy(equipment_attr_item.get('minorAttr'))

    varNames = {1: 'hp',
                2: 'atk',
                3: 'physicalDef',
                4: 'magicDef',
                5: 'hit',
                6: 'dodge',
                7: 'cri',
                8: 'criCoeff',
                9: 'criDedCoeff',
                10: 'block',
                11: 'ductility'}

    attr = {}
    for k, v in varNames.items():
        attr[v] = 0

    for k, v in main_pool.items():
        if k not in mainAttr:
            continue
        max_value = v[3]
        attr[varNames[k]] = attr[varNames[k]] + max_value

    for k, v in minor_pool.items():
        if k not in minorAttr:
            continue
        max_value = v[3]
        attr[varNames[k]] = attr[varNames[k]] + max_value

    formula = game_configs.formula_config.get("equFightValue").get("formula")
    assert formula!=None, "formula can not be None"
    max_result = eval(formula, attr)

    attr = {}
    for k, v in varNames.items():
        attr[v] = 0
    for k, v in mainAttr.items():
        max_value = v[1]
        attr[varNames[k]] = max_value

    for k, v in minorAttr.items():
        max_value = v[1]
        attr[varNames[k]] = attr.get(varNames[k], 0) + max_value

    formula = game_configs.formula_config.get("equFightValue").get("formula")
    assert formula!=None, "formula can not be None"
    result = eval(formula, attr)
    logger.debug("result/max_result")
    logger.debug(result)
    logger.debug(max_result)
    return result/float(max_result)


def rand_pick_attr(attr):
    attrType, attrValueType, attrValue, attrIncrement = -1, -1, -1, 0
    rand_pool = {}
    for at, v in attr.items():
        rand_pool[at] = int(v[0] * 100)
    rand = random.randint(0, sum(rand_pool.values()))

    for k, v in rand_pool.items():
        if v >= rand:
            attrType = k
            if len(attr[k]) == 5:
                _, attrValueType, valueMin, valueMax, attrIncrement = attr[k]
            else:
                _, attrValueType, valueMin, valueMax = attr[k]
            attrValue = int(valueMin + random.random() * (valueMax - valueMin))
            # add increment formula
            inputs = {'EquNumRandom': attrValue,'EquNumMax': valueMax, 'EquNumMin': valueMin, 'grow': attrIncrement}
            print(inputs)
            formula = game_configs.formula_config.get("equGrowUpParameter").get("formula")
            assert formula!=None, "formula can not be None"
            attrIncrement = eval(formula, inputs)
            logger.debug("increment value: %s %s" % (attrIncrement, attrIncrement))

            del attr[k]
            break
        else:
            rand -= v
    return attrType, attrValueType, attrValue, attrIncrement


class Equipment(object):
    """装备 """

    def __init__(self, character_id, equipment_id, equipment_name,
                 equipment_no,
                 strengthen_lv=1, awakening_lv=1, _enhance_info=None,
                 nobbing_effect={}, is_guard=False, main_attr={},
                 minor_attr={}, prefix=0, attr_id=0):

        _enhance_info = _enhance_info if _enhance_info else []
        nobbing_effect = nobbing_effect if nobbing_effect else {}
        main_attr = main_attr if main_attr else {}
        minor_attr = minor_attr if minor_attr else {}
        self._character_id = character_id
        self._base_info = EquipmentBaseInfoComponent(self,
                                                     equipment_id,
                                                     equipment_name,
                                                     equipment_no)
        self._attribute = EquipmentAttributeComponent(self,
                                                      strengthen_lv,
                                                      awakening_lv,
                                                      nobbing_effect,
                                                      is_guard,
                                                      main_attr,
                                                      minor_attr,
                                                      prefix, attr_id)
        self._record = EquipmentEnhanceComponent(self, _enhance_info)

    def add_data(self, character_id, attr_id=0):
        no = self._base_info.equipment_no
        mainAttr, minorAttr, prefix, equip_attr_id = init_equipment_attr(no, attr_id)
        self._attribute.main_attr = mainAttr
        self._attribute.minor_attr = minorAttr
        self._attribute.prefix = prefix
        self._attribute.attr_id = equip_attr_id
        data = dict(id=self._base_info.id,
                    equipment_info=dict(equipment_no=no,
                                        slv=self._attribute.strengthen_lv,
                                        alv=self._attribute.awakening_lv,
                                        is_guard=self._attribute.is_guard,
                                        main_attr=mainAttr,
                                        minor_attr=minorAttr,
                                        prefix=prefix,
                                        attr_id=equip_attr_id),
                    enhance_info=self._record.enhance_record,
                    nobbing_effect=self._attribute.nobbing_effect)

        char_obj = tb_character_info.getObj(character_id).getObj('equipments')
        result = char_obj.hsetnx(self._base_info.id, data)
        if not result:
            logger.error('add equipment error!:%s', self._base_info.id)

    def save_data(self):
        data = {'id': self._base_info.id,
                'equipment_info': {'equipment_no': self._base_info.equipment_no,
                                   'slv': self._attribute.strengthen_lv,
                                   'alv': self._attribute.awakening_lv,
                                   'is_guard': self._attribute.is_guard,
                                   'main_attr': self._attribute.main_attr,
                                   'minor_attr': self._attribute.minor_attr,
                                   'prefix': self._attribute.prefix,
                                   'attr_id': self._attribute.attr_id,
                                   },
                'enhance_info': self._record.enhance_record,
                'nobbing_effect': self._attribute.nobbing_effect}

        char_obj = tb_character_info.getObj(self._character_id).getObj('equipments')
        result = char_obj.hset(self._base_info.id, data)
        if not result:
            logger.error('save equipment error!:%s', self._base_info.id)

    def delete(self):
        char_obj = tb_character_info.getObj(self._character_id).getObj('equipments')
        result = char_obj.hdel(self._base_info.id)
        if not result:
            logger.error('del equipment error!:%s', self._base_info.id)

    @property
    def base_info(self):
        return self._base_info

    @property
    def attribute(self):
        return self._attribute

    def enhance(self, player):
        """强化
        """
        strength_max = player.base_info.level + self.strength_max
        before_lv = self._attribute.strengthen_lv
        enhance_lv = 1
        extra_enhance = self.get_extra_enhance_times(player) * enhance_lv
        print("extra_enhance=================", type(extra_enhance), type(before_lv))
        strengthen_lv = extra_enhance + before_lv
        if strengthen_lv > strength_max:
            strengthen_lv = strength_max
        self._attribute.strengthen_lv = strengthen_lv
        after_lv = self._attribute.strengthen_lv

        return before_lv, after_lv

    def get_extra_enhance_times(self, player):
        """ 获取强化暴击倍数
        return: 暴击倍数
        """
        items = player.base_info.equipment_strength_cli_times
        times = random_pick_with_percent(items)
        if times:
            return int(times)
        return 1

    def nobbing(self):
        """锤炼
        """
        pass

    @property
    def melting_item(self):
        """熔炼获得的配置物品
        """
        equipment_no = self._base_info.equipment_no
        equ_config_obj = game_configs.equipment_config.get(equipment_no, None)
        return equ_config_obj.gain

    @property
    def awakening_item(self):
        """觉醒需要装备，数量"""
        equipment_no = self._base_info.equipment_no
        equ_config_obj = game_configs.equipment_config.get(equipment_no, None)
        return equ_config_obj.awakening_item

    @property
    def suit_conf(self):
        """套装信息
        """
        equipment_no = self._base_info.equipment_no
        # 装备配置
        equ_conf_obj = game_configs.equipment_config.get(equipment_no, None)
        if not equ_conf_obj:
            return None
        suit_no = equ_conf_obj.suitNo
        suit_conf_obj = game_configs.set_equipment_config.get(suit_no)
        return suit_conf_obj

    def update_pb(self, equipment_pb):
        equipment_pb.id = self.base_info.id
        equipment_pb.no = self.base_info.equipment_no
        equipment_pb.strengthen_lv = self.attribute.strengthen_lv
        equipment_pb.awakening_lv = self.attribute.awakening_lv
        equipment_pb.is_guard = self.attribute.is_guard
        equipment_pb.prefix = self.attribute.prefix
        equipment_pb.attr_id = self.attribute.attr_id
        equipment_pb.nobbing_effect = 0
        equipment_pb.hero_no = 0

        for (attr_type, [attr_value_type, attr_value, attr_increment]) in self.attribute.main_attr.items():
            main_attr_pb = equipment_pb.main_attr.add()
            main_attr_pb.attr_type = attr_type
            main_attr_pb.attr_value_type = attr_value_type
            main_attr_pb.attr_value = attr_value
            main_attr_pb. attr_increment = attr_increment

        for (attr_type, [attr_value_type, attr_value, attr_increment]) in self.attribute.minor_attr.items():
            minor_attr_pb = equipment_pb.minor_attr.add()
            minor_attr_pb.attr_type = attr_type
            minor_attr_pb.attr_value_type = attr_value_type
            minor_attr_pb.attr_value = attr_value
            minor_attr_pb.attr_increment = attr_increment

        for before_lv, after_lv, enhance_cost in self._record.enhance_record:
            data_format = equipment_pb.data.add()
            data_format.before_lv = before_lv
            data_format.after_lv = after_lv
            data_format.cost_coin = enhance_cost
        #logger.debug("equipment_pb.data===============")
        #logger.debug(equipment_pb.attr_id)

    def calculate_attr(self, hero_self_attr):
        """根据属性和强化等级计算装备属性"""
        # hpEqu             装备加生命值    中间值  1   baseHp+growHp*equLevel
        # atkEqu            装备加攻击力    中间值  1   baseAtk+growAtk*equLevel
        # physicalDefEqu    装备加物防  中间值  1   basePdef+growPdef*equLevel
        # magicDefEqu       装备加魔防  中间值  1   baseMdef+growMdef*equLevel
        # hitEqu            装备加命中  中间值  1   hit
        # dodgeEqu          装备加闪避  中间值  1   dodge
        # criEqu            装备加暴击  中间值  1   cri
        # criCoeffEqu       装备加暴伤  中间值  1   criCoeff
        # criDedCoeffEqu    装备加暴免  中间值  1   criDedCoeff
        # blockEqu          装备加格挡  中间值  1   block
        # ductilityEqu      装备加韧性  中间值  1   ductility

        # 1：加生命值上限
        # 2：加攻击力
        # 3：加物理防御
        # 4：加魔法防御
        # 5：加命中率
        # 6：加闪避率
        # 7：暴击率
        # 8：加暴击伤害
        # 9：加暴伤减免
        # 10：加格挡率
        # 11：加韧性

        result = {}
        varNames = {1: 'baseHp',
                    2: 'baseAtk',
                    3: 'basePdef',
                    4: 'baseMdef',
                    5: 'hit',
                    6: 'dodge',
                    7: 'cri',
                    8: 'criCoeff',
                    9: 'criDedCoeff',
                    10: 'block',
                    11: 'ductility'}
        varNames2 = {1: 'growHp',
                     2: 'growAtk',
                     3: 'growPdef',
                     4: 'growMdef',
                     5: 'growHit',
                     6: 'growDodge',
                     7: 'growCri',
                     8: 'growCriCoeff',
                     9: 'growCriDedCoeff',
                     10: 'growBlock',
                     11: 'growDuctility'
                     }
        varNames3 = {1: 'hpHero',
                     2: 'atkHero',
                     3: 'physicalDefHero',
                     4: 'magicDefHero'}

        allVars = dict(baseHp=0,
                       baseAtk=0,
                       basePdef=0,
                       baseMdef=0,
                       hit=0,
                       dodge=0,
                       cri=0,
                       criCoeff=0,
                       criDedCoeff=0,
                       block=0,
                       ductility=0,
                       growHp=0,
                       growAtk=0,
                       growPdef=0,
                       growMdef=0,
                       growHit=0,
                       growDodge=0,
                       growCri=0,
                       growCriCoeff=0,
                       growCriDedCoeff=0,
                       growBlock=0,
                       growDuctility=0,
                       equLevel=self._attribute.strengthen_lv)

        for k, v in self._attribute.main_attr.items():
            assert varNames[k] in allVars
            avt, av, ai = v
            if avt == 1:
                allVars[varNames[k]] += av
                if k in varNames2:
                    allVars[varNames2[k]] += ai
            elif avt == 2:
                if k not in varNames3:
                    allVars[varNames2[k]] += (av*hero_self_attr.get(varNames3[k], 0))
                else:
                    raise Exception('error %s:%s:%s' % avt, k, varNames3[k])
        for k, v in self._attribute.minor_attr.items():
            assert varNames[k] in allVars
            avt, av, ai = v
            if avt == 1:
                allVars[varNames[k]] += av
                if k in varNames2:
                    allVars[varNames2[k]] += ai
            elif avt == 2:
                if k not in varNames3:
                    allVars[varNames2[k]] += (av*hero_self_attr.get(varNames3[k], 0))
                else:
                    raise Exception('error %s:%s:%s' % avt, k, varNames3[k])

        formulas = dict(hp='hpEqu',
                        atk='atkEqu',
                        physical_def='physicalDefEqu',
                        magic_def='magicDefEqu',
                        hit='hitEqu',
                        dodge='dodgeEqu',
                        cri='criEqu',
                        cri_coeff='criCoeffEqu',
                        cri_ded_coeff='criDedCoeffEqu',
                        block='blockEqu',
                        ductility='ductilityEqu')

        for k, v in formulas.items():
            formula = game_configs.formula_config.get(v)
            if not formula:
                raise Exception('cant find formula by name:%s' % k)
            result[k] = eval(formula.formula, allVars, allVars)

        # print 'result:'*4, self._base_info.equipment_no, result
        # print '-'*32
        # print 'allVars:', allVars
        # print '='*32

        return CommonItem(result)

    @property
    def strength_max(self):
        """获取装备上限为玩家等级+strength_max"""
        return game_configs.base_config.get("max_equipment_strength")

    @property
    def enhance_record(self):
        return self._record

    @property
    def equipment_config_info(self):
        equipment_no = self._base_info.equipment_no
        equ_config_obj = game_configs.equipment_config.get(equipment_no)
        assert equ_config_obj is not None, "equipment id: %s can not find config info" % equipment_no
        return equ_config_obj
