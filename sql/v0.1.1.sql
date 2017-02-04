ALTER TABLE `post` MODIFY COLUMN `posted_at` int unsigned NOT NULL DEFAULT 0 COMMENT '帖子发布时间';
ALTER TABLE `post_tag` ADD UNIQUE u_tag_name(`tag_name`);