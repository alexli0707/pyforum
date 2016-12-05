-- ----------------------------
--  Table structure for `users`
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(64) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `role_id` TINYINT(4)  DEFAULT 0 NOT NULL COMMENT '角色id',
  `confirmed` tinyint(1) unsigned DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 后台路由模块表
CREATE TABLE `manage_module` (
  `id`        INT(10) UNSIGNED        NOT NULL AUTO_INCREMENT,
  `parent_id` INT(10) UNSIGNED        NOT NULL DEFAULT '0'
  COMMENT '上级模块id',
  `name`      VARCHAR(20)
              COLLATE utf8_unicode_ci NOT NULL DEFAULT ''
  COMMENT '模块名称',
  `uri`       VARCHAR(50)
              COLLATE utf8_unicode_ci NOT NULL DEFAULT ''
  COMMENT '路径',
  `prefix`    VARCHAR(50)
              COLLATE utf8_unicode_ci NOT NULL DEFAULT ''
  COMMENT 'uri前缀',
  `weight`    SMALLINT(5) UNSIGNED    NOT NULL DEFAULT '0'
  COMMENT '权重越大越靠前',
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COMMENT = '后台功能模块表';


#用户角色说明------ 开始
CREATE TABLE `user_role` (
  `id`  TINYINT(4)   NOT NULL
  COMMENT '角色id',
  `des` VARCHAR(100) NOT NULL  DEFAULT ''
  COMMENT '角色说明',
  PRIMARY KEY (`id`)
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COMMENT = '用户角色说明表';
INSERT INTO `user_role` (id, des) VALUES (0, '普通用户');
INSERT INTO `user_role` (id, des) VALUES (20, '小编');
INSERT INTO `user_role` (id, des) VALUES (99, '管理员');
#用户角色说明------ 结束

#角色模块表 -----开始

DROP TABLE IF EXISTS `role_module`;
CREATE TABLE `role_module` (
  `id`        INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `role_id`   TINYINT(4)       NOT NULL DEFAULT 20
  COMMENT '用户角色id, 20:合作商 99:管理员',
  `module_id` INT(10) UNSIGNED NOT NULL
  COMMENT '模块id',
  PRIMARY KEY (`id`),
  CONSTRAINT `role_module_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `user_role` (`id`)
    ON UPDATE CASCADE
    ON DELETE CASCADE
)
  ENGINE = InnoDB
  DEFAULT CHARSET = utf8
  COMMENT = '角色-模块表';


#角色模块表 -----结束
