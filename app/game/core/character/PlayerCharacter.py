# -*- coding:utf-8 -*-
"""
created by server on 14-6-4下午3:04.
"""

from app.game.core.character.Character import Character
from datetime import datetime
from shared.utils.const import const


class PlayerCharacter(Character):
    """玩家角色类
    """

    def __init__(self, cid, name=u'城管', dynamic_id=-1, status=1):
        """构造方法
        @dynamic_id （int） 角色登陆的动态ID socket连接产生的id
        """
        Character.__init__(self, cid, name)

        self.character_type = const.PLAYERTYPE  # 设置角色类型为玩家角色
        self.dynamic_id = dynamic_id   # 角色登陆服务器时的动态id
        #--------角色的各个组件类------------
        # TODO

        if status:
            self.initPlayerInfo()  #初始化角色

    def __init_player_info(self):
        """初始化角色信息
        """
        pid = self.base_info.id
        pmmode = tb_character_admin.getObj(pid)
        data = pmmode.get("data")
        if not data:
            print "Inint_player _" + str(self.baseInfo.id)
        #------------初始化角色基础信息组件---------
        pass


    def getDynamicId(self):
        '''获取角色的动态Id'''
        return self.dynamicId

    def formatInfo(self):
        '''格式化角色基本信息'''
        attrinfo = self.attribute.getCharacterAttr()
        characterInfo = {}
        characterInfo['id'] = self.baseInfo.id  #角色的ID
        characterInfo['nickname'] = self.baseInfo.getNickName()  #角色的昵称
        characterInfo['roletype'] = self.baseInfo.getType()
        characterInfo['vipexp'] = self.level.getVipExp()
        characterInfo['level'] = self.level.getLevel()
        characterInfo['profession'] = self.profession.getFigure()
        characterInfo['energy'] = self.attribute.getEnergy()
        characterInfo['rank'] = ''  #self.rank.getRankName()
        characterInfo['guildname'] = u''  #self.guild.getGuildInfo().get('name','')

        characterInfo['manualStr'] = attrinfo.get('Str', 0)
        characterInfo['manualDex'] = attrinfo.get('Dex', 0)
        characterInfo['manualVit'] = attrinfo.get('Vit', 0)
        characterInfo['manualWis'] = attrinfo.get('Wis', 0)
        characterInfo['maxHp'] = int(self.attribute.getMaxHp())
        characterInfo['hp'] = int(self.attribute.getHp())
        characterInfo['exp'] = int(self.level.getExp())
        characterInfo['maxExp'] = int(self.level.getMaxExp())

        characterInfo['physicalAttack'] = attrinfo.get('PhyAtt', 0)
        characterInfo['magicAttack'] = attrinfo.get('MigAtt', 0)
        characterInfo['physicalDefense'] = attrinfo.get('PhyDef', 0)
        characterInfo['magicDefense'] = attrinfo.get('MigDef', 0)
        characterInfo['speed'] = attrinfo.get('Speed', 0)
        characterInfo['dodgeRate'] = attrinfo.get('Dodge', 0)
        characterInfo['critRate'] = attrinfo.get('CriRate', 0)
        characterInfo['block'] = attrinfo.get('Block', 0)
        characterInfo['hitRate'] = attrinfo.get('HitRate', 0)

        characterInfo['coin'] = self.finance.getCoin()
        characterInfo['gold'] = self.finance.getGold()
        return characterInfo

    def CheckClient(self, dynamicId):
        '''检测客户端id是否匹配'''
        if self.dynamicId == dynamicId:
            return True
        return False

    def updatePlayerDBInfo(self):
        '''更新角色在数据库中的数据'''
        pid = self.baseInfo.id
        pmmode = tb_character_admin.getObj(pid)
        mapping = {'level': self.level.getLevel(), 'coin': self.finance.getCoin(),
                   'gold': self.finance.getGold(), 'exp': self.level.getExp(),
                   'energy': self.attribute.getEnergy(), 'outtime': datetime.now()}
        pmmode.update_multi(mapping)

        self.pack._equipmentSlot.updateEquipments(self.baseInfo.id)

    def getFightData(self, preDict={'extVitper': 0, 'extStrper': 0,
                                    'extDexper': 0, 'extWisper': 0, 'extSpiper': 0}):
        '''获取战斗数据'''
        attrinfo = self.attribute.getCharacterAttr()
        fightdata = {}
        fightdata['chaId'] = self.baseInfo.id  #角色的ID
        fightdata['chaName'] = self.baseInfo.getNickName()  #角色的昵称
        fightdata['chaLevel'] = self.level.getLevel()  #角色的等级
        fightdata['characterType'] = self.CharacterType  #角色的类型  1:玩家角色 2:怪物 3:宠物
        fightdata['figureType'] = self.profession.getFightFigure()  #角色形象类型
        fightdata['chaBattleId'] = 0  #角色在战场中的id
        fightdata['difficulty'] = 0  #怪物难度
        fightdata['chaProfessionType'] = self.profession.getFightFigure()  #角色的角色形象ID
        fightdata['chaIcon'] = self.profession.getProfession()
        fightdata['chatype'] = 0
        fightdata['chaDirection'] = 1  #(角色在战斗中的归属阵营)1--(主动方)玩家朝向右，朝向右。2(被动方)--玩家朝向左
        fightdata['chaCurrentHp'] = self.attribute.getMaxHp()  #角色当前血量
        fightdata['chaCurrentPower'] = attrinfo.get('power', 0)  #角色的当前能量#角色的当前能量
        fightdata['chaTotalHp'] = self.attribute.getMaxHp()  #角色的最大血量
        fightdata['chaTotalPower'] = Character.MAXPOWER  #角色的最大能量
        fightdata['chaPos'] = (0, 0)  #角色的坐标
        fightdata['physicalAttack'] = attrinfo.get('PhyAtt', 0)
        fightdata['magicAttack'] = attrinfo.get('MigAtt', 0)  #角色的魔法攻击
        fightdata['physicalDefense'] = attrinfo.get('PhyDef', 0)  #角色的物理防御
        fightdata['magicDefense'] = attrinfo.get('MigDef', 0)  #角色的魔法防御
        fightdata['speed'] = attrinfo.get('Speed', 0)  #角色的攻速
        fightdata['hitRate'] = attrinfo.get('HitRate', 0)  #角色的命中
        fightdata['critRate'] = attrinfo.get('CriRate', 0)  #角色的当前暴击率
        fightdata['block'] = attrinfo.get('Block', 0)  #角色的抗暴率
        fightdata['dodgeRate'] = attrinfo.get('Dodge', 0)  #角色的闪避几率
        fightdata['ActiveSkillList'] = attrinfo.get('Skill', [])  #self.skill.getActiveSkillList()#角色的主动攻击技能
        fightdata['ordSkill'] = self.profession.getOrdinarySkill()  #角色的普通攻击技能
        fightdata['canDoMagicSkill'] = 1  #可否释放魔法技能
        fightdata['canDoPhysicalSkill'] = 1  #可否释放物理技能
        fightdata['canDoOrdSkill'] = 1  #可否进行普通攻击
        fightdata['canBeTreat'] = 1  #可否被治疗
        fightdata['canBeAttacked'] = 1  #可否被攻击
        fightdata['canDied'] = 1  #是否可死亡
        fightdata['skillIDByAttack'] = 0  #被攻击的技能的ID 普通攻击为 0
        fightdata['expbound'] = 0  #经验奖励
        fightdata['chaPz'] = 0
        fightdata['equip'] = {}  #self.pack.getAllEquipttributes()
        return fightdata

    def formatInfoForWeiXin(self):
        '''格式化角色信息
        '''
        attrinfo = self.attribute.getCharacterAttr()
        info = {}
        info['chaid'] = self.baseInfo.id
        info['rolename'] = self.baseInfo.getNickName()
        info['icon'] = self.profession.getProfession()
        info['level'] = self.level.getLevel()
        guanqiainfo = {}
        info['guanqia'] = u'无' if not guanqiainfo else guanqiainfo['name']
        skill = attrinfo.get('Skill', [])
        if skill:
            skillinfo = dbSkill.ALL_SKILL_INFO.get(skill[0])
        else:
            skillinfo = None
        info['skill'] = u'无' if not skillinfo else skillinfo['skillName']
        info['attack'] = attrinfo.get('PhyAtt', 0)
        info['fangyu'] = attrinfo.get('PhyDef', 0)
        info['tili'] = self.attribute.getMaxHp()
        info['minjie'] = attrinfo.get('Speed', 0)
        info['price'] = self.level.getLevel() * 1000
        return info
        
