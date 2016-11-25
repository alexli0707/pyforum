-- ----------------------------
--  Table structure for `users`
-- ----------------------------
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `confirmed` tinyint(1) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;