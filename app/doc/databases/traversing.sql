-- MySQL dump 10.13  Distrib 5.6.21, for osx10.8 (x86_64)
--
-- Host: localhost    Database: traversing_1
-- ------------------------------------------------------
-- Server version	5.6.21


--
-- Table structure for table `tb_character_activity`
--

DROP TABLE IF EXISTS `tb_character_activity`;
CREATE TABLE `tb_character_activity` (
  `id` bigint(20) NOT NULL,
  `sign_in` blob,
  `online_gift` blob,
  `level_gift` blob,
  `feast` int(11) DEFAULT '0',
  `login_gift` blob,
  `world_boss` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_equipment_chip`
--

DROP TABLE IF EXISTS `tb_character_equipment_chip`;
CREATE TABLE `tb_character_equipment_chip` (
  `id` bigint(20) NOT NULL,
  `chips` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_friend`
--

DROP TABLE IF EXISTS `tb_character_friend`;
CREATE TABLE `tb_character_friend` (
  `id` bigint(20) NOT NULL,
  `friends` blob,
  `blacklist` blob,
  `applicants_list` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_guild`
--

DROP TABLE IF EXISTS `tb_character_guild`;
CREATE TABLE `tb_character_guild` (
  `id` varchar(32) NOT NULL,
  `info` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_hero`
--

DROP TABLE IF EXISTS `tb_character_hero`;
CREATE TABLE `tb_character_hero` (
  `id` varchar(50) NOT NULL,
  `character_id` bigint(20) NOT NULL,
  `property` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_hero_chip`
--

DROP TABLE IF EXISTS `tb_character_hero_chip`;
CREATE TABLE `tb_character_hero_chip` (
  `id` varchar(50) NOT NULL,
  `hero_chips` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_info`
--

DROP TABLE IF EXISTS `tb_character_info`;
CREATE TABLE `tb_character_info` (
  `id` bigint(20) NOT NULL,
  `nickname` varchar(128) DEFAULT '',
  `level` int(11) NOT NULL DEFAULT '1',
  `exp` int(11) NOT NULL DEFAULT '0',
  `fine_hero_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `excellent_hero_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `fine_equipment_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `excellent_equipment_last_pick_time` int(11) NOT NULL DEFAULT '0',
  `pvp_times` int(11) DEFAULT 0,
  `pvp_refresh_time` int(11) DEFAULT 0,
  `get_stamina_times` int(11) NOT NULL DEFAULT '0',
  `last_login_time` int(11) DEFAULT NULL,
  `vip_level` int(11) NOT NULL DEFAULT '0',
  `create_time` int(11) NOT NULL DEFAULT '0',
  `newbee_guide_id` int(11) NOT NULL DEFAULT '0',
  `finances` tinyblob,
  `stamina` blob NOT NULL,
  `brew` blob,
  `hero_refine` blob,
  PRIMARY KEY (`id`),
  KEY `nickname` (`nickname`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_character_shop`;
CREATE TABLE `tb_character_shop` (
  `id` bigint(20) NOT NULL,
  `shop` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
--
-- Table structure for table `tb_character_item_package`
--

DROP TABLE IF EXISTS `tb_character_item_package`;
CREATE TABLE `tb_character_item_package` (
  `id` bigint(10) NOT NULL,
  `items` mediumblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_line_up`
--

DROP TABLE IF EXISTS `tb_character_line_up`;
CREATE TABLE `tb_character_line_up` (
  `id` bigint(20) NOT NULL,
  `line_up_slots` blob,
  `sub_slots` blob,
  `line_up_order` blob,
  `unpars` tinyblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_lord`
--

DROP TABLE IF EXISTS `tb_character_lord`;
CREATE TABLE `tb_character_lord` (
  `id` bigint(20) NOT NULL,
  `attr_info` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_character_stages`
--

DROP TABLE IF EXISTS `tb_character_stages`;
CREATE TABLE `tb_character_stages` (
  `id` bigint(20) NOT NULL,
  `stage_info` blob,
  `award_info` blob,
  `elite_stage` blob,
  `act_stage` blob,
  `sweep_times` blob NOT NULL,
  `stage_up_time` bigint(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_equipment_info`
--

DROP TABLE IF EXISTS `tb_equipment_info`;
CREATE TABLE `tb_equipment_info` (
  `id` varchar(32) NOT NULL,
  `character_id` bigint(20) NOT NULL,
  `equipment_info` blob,
  `enhance_info` blob,
  `nobbing_effect` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_guild_info`
--

DROP TABLE IF EXISTS `tb_guild_info`;
CREATE TABLE `tb_guild_info` (
  `id` varchar(32) NOT NULL,
  `info` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_guild_name`
--

DROP TABLE IF EXISTS `tb_guild_name`;
CREATE TABLE `tb_guild_name` (
  `g_name` varchar(32) NOT NULL,
  `g_id` varchar(32) NOT NULL,
  PRIMARY KEY (`g_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_mail_info`
--

DROP TABLE IF EXISTS `tb_mail_info`;
CREATE TABLE `tb_mail_info` (
  `id` varchar(50) NOT NULL,
  `character_id` bigint(20) NOT NULL,
  `property` blob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `tb_pvp_rank`
--

DROP TABLE IF EXISTS `tb_pvp_rank`;
CREATE TABLE `tb_pvp_rank` (
  `id` bigint(20) NOT NULL,
  `character_id` bigint(20) NOT NULL,
  `nickname` varchar(128) DEFAULT '',
  `level` int(11) NOT NULL DEFAULT '1',
  `ap` int(11) NOT NULL,
  `best_skill` int(11) NOT NULL,
  `unpar_skill` int(11) NOT NULL,
  `unpar_skill_level` int(11) NOT NULL,
  `units` blob NOT NULL,
  `slots` blob NOT NULL,
  `hero_ids` tinyblob NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_character_travel`;
CREATE TABLE `tb_character_travel` (
  `id` bigint(20) NOT NULL,
  `travel` blob,
  `travel_item` blob,
  `shoes` blob,
  `fight_cache` blob,
  `chest_time` bigint(20),
  `auto` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tb_character_lively`;
CREATE TABLE `tb_character_lively` (
  `id` bigint(20) NOT NULL,
  `lively` int(11) NOT NULL,
  `tasks` blob,
  `event_map` blob,
  `last_day` varchar(8),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `tb_character_stone`;
CREATE TABLE `tb_character_stone` (
  `id` bigint(20) NOT NULL,
  `stones` mediumblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `tb_character_mine`;
CREATE TABLE `tb_character_mine` (
  `id` bigint(20) NOT NULL,
  `reset_day` varchar(8) NOT NULL,
  `reset_times` int(11) NOT NULL,
  `day_before` varchar(8) NOT NULL,
  `lively` int(11) NOT NULL,
  `mine` mediumblob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `tb_character_runt`;
CREATE TABLE `tb_character_runt` (
  `id` bigint(20) NOT NULL,
  `m_runt` mediumblob,
  `stone1` int(11),
  `stone2` int(11),
  `refresh_runt` blob,
  `refresh_times` blob,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
