#-*-coding:utf8-*-


from shared.db_entrust.redis_mode import MAdmin

tb_account = MAdmin('tb_account', 'id')  # 帐号表
tb_account.insert()

tb_account_mapping = MAdmin('tb_account_mapping', 'account_token')  # 帐号匹配表
tb_account_mapping.insert()

# 用户信息表
tb_character_info = MAdmin('tb_character_info', 'id')
tb_character_info.insert()

# 用户英雄信息表
tb_character_heros = MAdmin('tb_character_heros', 'id')
tb_character_heros.insert()

# 英雄信息表
tb_character_hero = MAdmin('tb_character_hero', 'id', 1800)
tb_character_hero.insert()

# 用户英雄碎片信息表
tb_character_hero_chip = MAdmin('tb_character_hero_chip', 'id', 1800)
tb_character_hero_chip.insert()

# 用户道具背包
tb_character_item_package = MAdmin('tb_character_item_package', 'id')
tb_character_item_package.insert()

# 用户阵容信息
tb_character_line_up = MAdmin('tb_character_line_up', 'id')
tb_character_line_up.insert()

# 用户装备列表
tb_character_equipments = MAdmin('tb_character_equipments', 'id')
tb_character_equipments.insert()

# 装备信息表
tb_equipment_info = MAdmin('tb_equipment_info', 'id')
tb_equipment_info.insert()

# 装备碎片表
tb_character_equipment_chip = MAdmin('tb_character_equipment_chip', 'id')
tb_character_equipment_chip.insert()

# friend表
tb_character_friend = MAdmin('tb_character_friend', 'id')
tb_character_friend.insert()
