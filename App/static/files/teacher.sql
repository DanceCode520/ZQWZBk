/*
Navicat MySQL Data Transfer

Source Server         : zltwz
Source Server Version : 50726
Source Host           : localhost:3306
Source Database       : zqwz

Target Server Type    : MYSQL
Target Server Version : 50726
File Encoding         : 65001

Date: 2020-11-05 07:49:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `pwd` varchar(255) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `sex` tinyint(11) DEFAULT NULL,
  `signature` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `privilege_level` int(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `grade` varchar(255) DEFAULT NULL,
  `update_time` datetime DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `nation` varchar(255) DEFAULT NULL,
  `isdel` tinyint(4) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('1', '张金阳99', '999999', '2019-05-23', '1', '我很喜欢学生', '扎旗一中阿尔泰3楼', '1', '123', '1.jpg', '九年二班&&&七年五班&&&八年六班', '2020-10-30 08:59:27', '汉族', '0');
INSERT INTO `teacher` VALUES ('2', 'michael', '484', '2019-05-23', '1', '我天下无敌', '扎旗一中阿尔泰3楼', '1', '125', '1.jpg', '九年二班&&&七年五班&&&八年六班', '2020-10-30 08:59:10', '满族', '0');
INSERT INTO `teacher` VALUES ('4', 'michael', '888', '2019-05-23', '1', '我才华横溢', '扎旗一中阿尔泰3楼', '1', '19888888888', '1.jpg', '九年二班&&&七年五班&&&八年六班', '2020-10-29 11:23:25', '苗族', '0');
INSERT INTO `teacher` VALUES ('5', '张金阳', '888', '2019-05-23', '1', '我很喜欢学生', '扎旗一中阿尔泰3楼', '1', '19888888888', '1.jpg', '九年二班&&&七年五班&&&八年六班', '2020-10-29 17:03:52', '汉族', '1');
INSERT INTO `teacher` VALUES ('6', '张金阳', '888', '2019-05-23', '1', '我很喜欢学生', '扎旗一中阿尔泰3楼', '1', '19888888888', '1.jpg', '九年二班&&&七年五班&&&八年六班', '2015-02-22 08:08:08', '汉族', '0');
INSERT INTO `teacher` VALUES ('8', '李晓明', '484', '2020-05-23', '1', 'new我很喜欢学生', 'new扎旗一中阿尔泰3楼', '1', '254', 'new1.jpg', 'new九年二班&&&七年五班&&&八年六班', '2020-10-30 15:22:09', '汉族new', '0');
