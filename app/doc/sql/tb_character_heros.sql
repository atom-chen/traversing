DROP TABLE IF EXISTS `tb_character_heros`;

CREATE TABLE `tb_character_heros` (
  `id` varchar(50),
  `hero_ids` blob NOT NULL,
 PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;