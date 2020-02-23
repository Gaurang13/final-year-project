CREATE DATABASE IF NOT EXISTS `blind_eyes`;
USE `blind_eyes`;

DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`
(
    `id`           bigint(20) unsigned    NOT NULL AUTO_INCREMENT,
    `first_name`   varchar(50)         NOT NULL,
    `last_name`    varchar(50)         NOT NULL,
    `email`        varchar(50)         NOT NULL,
    `password`     varchar(50)         NOT NULL,
    `phone_number` varchar(15)         NOT NULL,
    `created_at`   datetime(3)         NOT NULL,
    PRIMARY KEY (`id`),
    UNIQUE KEY `uk_user_email` (`email`),
    UNIQUE KEY `uk_user_phone_number` (`phone_number`)
) ENGINE = InnoDB
  DEFAULT CHARSET = latin1;


DROP TABLE IF EXISTS `text`;

CREATE TABLE `text`
(
    `id`               bigint(20) unsigned    NOT NULL AUTO_INCREMENT,
    `text`             varchar(100)    NOT NULL,
    `user_id`          bigint(20) unsigned NOT NULL,
    `created_at`       datetime(3)         NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fk_text_user_id` (`user_id`),
    CONSTRAINT `fk_text_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = latin1;


DROP TABLE IF EXISTS `text_response`;

CREATE TABLE `text_response`
(
    `id`                  bigint(20) unsigned    NOT NULL AUTO_INCREMENT,
    `text_id`             bigint(20) unsigned    NOT NULL,
    `command_id`          bigint(20) unsigned    NOT NULL,
    `created_at`       datetime(3)         NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fk_text_user_id` (`user_id`),
    CONSTRAINT `fk_text_user_id` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE = InnoDB
  DEFAULT CHARSET = latin1;
