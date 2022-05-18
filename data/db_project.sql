/*
 Navicat MySQL Data Transfer

 Source Server         : wz
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : db_project

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 11/06/2020 23:28:38
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for branch
-- ----------------------------
DROP TABLE IF EXISTS `branch`;
CREATE TABLE `branch`  (
  `bid` int(0) NOT NULL AUTO_INCREMENT,
  `bname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `postcode` varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`bid`) USING BTREE,
  INDEX `PostCode`(`postcode`) USING BTREE,
  INDEX `bid`(`bid`) USING BTREE,
  INDEX `bid_2`(`bid`) USING BTREE,
  INDEX `bid_3`(`bid`) USING BTREE,
  CONSTRAINT `Branch_ibfk_1` FOREIGN KEY (`postcode`) REFERENCES `location` (`postcode`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of branch
-- ----------------------------
INSERT INTO `branch` VALUES (1, 'add a record', 'test@gmail.com', '1111', '4000');
INSERT INTO `branch` VALUES (2, 'sia', '1321@qq.com', '5039432873', '4001');
INSERT INTO `branch` VALUES (3, 'sawr', '1321@qq.com', '5039432875', '4003');
INSERT INTO `branch` VALUES (4, 'See', '1234@qq.com', '12345', '4002');
INSERT INTO `branch` VALUES (5, 'Aklie', 'sdw@gmail.com', '5039432875', '4005');
INSERT INTO `branch` VALUES (6, 'zhe wang', '1111@gmail.com', '1221311', '4005');

-- ----------------------------
-- Table structure for dependents
-- ----------------------------
DROP TABLE IF EXISTS `dependents`;
CREATE TABLE `dependents`  (
  `mid` int(0) NOT NULL,
  `pname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `age` int(0) NOT NULL,
  `cost` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`mid`, `pname`) USING BTREE,
  CONSTRAINT `Dependents_ibfk_1` FOREIGN KEY (`mid`) REFERENCES `member` (`mid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dependents
-- ----------------------------
INSERT INTO `dependents` VALUES (1, 'ds', 22, 111);
INSERT INTO `dependents` VALUES (2, 'reas', 11, 111);
INSERT INTO `dependents` VALUES (4, 'jun', 26, 1000);
INSERT INTO `dependents` VALUES (5, 'eric', 21, 1000);
INSERT INTO `dependents` VALUES (5, 'Martin', 23, 900);

-- ----------------------------
-- Table structure for employee
-- ----------------------------
DROP TABLE IF EXISTS `employee`;
CREATE TABLE `employee`  (
  `eid` int(0) NOT NULL,
  `fname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `lname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `salary` int(0) NOT NULL,
  `gender` char(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `mid` int(0) NOT NULL,
  `bid` int(0) NOT NULL,
  `password` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `is_internship` int(1) UNSIGNED ZEROFILL NULL DEFAULT NULL,
  `username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`eid`) USING BTREE,
  INDEX `MID`(`mid`) USING BTREE,
  INDEX `BID`(`bid`) USING BTREE,
  INDEX `eid`(`eid`) USING BTREE,
  CONSTRAINT `Emploee_ibfk_2` FOREIGN KEY (`bid`) REFERENCES `branch` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`mid`) REFERENCES `employee` (`eid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of employee
-- ----------------------------
INSERT INTO `employee` VALUES (1, 'da', 'da', 'fsd@gmail.com', '21231', 231, 'male', 1, 2, '123', 0, 'eric');
INSERT INTO `employee` VALUES (3, 'da', 'das', 'sdf@gmail.com', '312', 1212, 'female', 3, 3, '123', 1, 'sfas');
INSERT INTO `employee` VALUES (4, 'das', 'eedw', 'test@mail.com', '11231', 222, 'female', 4, 2, '123', 1, 'edada');

-- ----------------------------
-- Table structure for facility
-- ----------------------------
DROP TABLE IF EXISTS `facility`;
CREATE TABLE `facility`  (
  `fid` int(0) NOT NULL,
  `status_label` varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `manufactory` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `manufacture_date` date NULL DEFAULT NULL,
  `eid` int(0) NOT NULL,
  `is_outdoor` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`fid`) USING BTREE,
  INDEX `EID`(`eid`) USING BTREE,
  CONSTRAINT `facility_ibfk_1` FOREIGN KEY (`eid`) REFERENCES `employee` (`eid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of facility
-- ----------------------------
INSERT INTO `facility` VALUES (1, 'bad', 'dasd', '2020-06-25', 3, 0);
INSERT INTO `facility` VALUES (2, 'bad', 'fasa', '2020-06-03', 3, 1);
INSERT INTO `facility` VALUES (3, 'bad', 'sweq', '2020-06-07', 1, 0);
INSERT INTO `facility` VALUES (4, 'good', 'sasgw', '2020-06-01', 4, 1);
INSERT INTO `facility` VALUES (5, 'sileve', 'sas', '2020-06-05', 1, 1);

-- ----------------------------
-- Table structure for home
-- ----------------------------
DROP TABLE IF EXISTS `home`;
CREATE TABLE `home`  (
  `id` int(0) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `content` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `image` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of home
-- ----------------------------
INSERT INTO `home` VALUES (1, 'welcome to our fitness', ' let\'s get start', '1.jpg');
INSERT INTO `home` VALUES (2, 'Thanks for joining us', 'challenge yourself right now', '2.jpg');
INSERT INTO `home` VALUES (3, 'Grauduation', 'get a chance to make your friend', '3.jpg');

-- ----------------------------
-- Table structure for location
-- ----------------------------
DROP TABLE IF EXISTS `location`;
CREATE TABLE `location`  (
  `postcode` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `address` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`postcode`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of location
-- ----------------------------
INSERT INTO `location` VALUES ('4000', 'St.lucia');
INSERT INTO `location` VALUES ('4001', 'southbank');
INSERT INTO `location` VALUES ('4002', 'sunnybank');
INSERT INTO `location` VALUES ('4003', 'gold coast');
INSERT INTO `location` VALUES ('4004', 'screte street');
INSERT INTO `location` VALUES ('4005', 'local');

-- ----------------------------
-- Table structure for member
-- ----------------------------
DROP TABLE IF EXISTS `member`;
CREATE TABLE `member`  (
  `mid` int(0) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `lname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `phone` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `address` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `email` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  `gender` char(10) CHARACTER SET latin2 COLLATE latin2_general_ci NOT NULL DEFAULT '',
  `bid` int(0) NOT NULL,
  `mtype` varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `password` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL DEFAULT '',
  PRIMARY KEY (`mid`) USING BTREE,
  INDEX `BID`(`bid`) USING BTREE,
  INDEX `MType`(`mtype`) USING BTREE,
  CONSTRAINT `Member_ibfk_1` FOREIGN KEY (`bid`) REFERENCES `branch` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Member_ibfk_2` FOREIGN KEY (`mtype`) REFERENCES `membership` (`mtype`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of member
-- ----------------------------
INSERT INTO `member` VALUES (1, 'sa', 'wag', '12131', 'faw', '212@gmail.com', 'male', 1, 'platinum', '123', 'mope');
INSERT INTO `member` VALUES (2, 'sa', 'wadf', '131', 'wsd', 'fas@gmail.com', 'female', 6, 'silver', '123', 'msol');
INSERT INTO `member` VALUES (4, 'Kavein', 'King', '5039432875', 'sunnybank', '1321@qq.com', 'male', 3, 'gold', '123', 'Msoewl');
INSERT INTO `member` VALUES (5, 'dasd', 'ddd', '5039432875', 'gold coast', '222@qq.com', 'male', 2, 'brass', '123', 'Mow');
INSERT INTO `member` VALUES (6, 'martin', 'wang', '1234', 'goal cost', '23124@gmail.com', 'male', 2, 'brass', '122141241', 'Mopos');

-- ----------------------------
-- Table structure for membership
-- ----------------------------
DROP TABLE IF EXISTS `membership`;
CREATE TABLE `membership`  (
  `mtype` varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `priviliege_description` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  PRIMARY KEY (`mtype`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of membership
-- ----------------------------
INSERT INTO `membership` VALUES ('brass', 'read only');
INSERT INTO `membership` VALUES ('gold', 'team sport');
INSERT INTO `membership` VALUES ('king', 'everything');
INSERT INTO `membership` VALUES ('platinum', 'control');
INSERT INTO `membership` VALUES ('silver', 'join');

-- ----------------------------
-- Table structure for private_coach
-- ----------------------------
DROP TABLE IF EXISTS `private_coach`;
CREATE TABLE `private_coach`  (
  `rid` int(0) NOT NULL AUTO_INCREMENT,
  `fname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `lname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `teaching_age` int(0) NOT NULL,
  `gender` char(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `email` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `phone` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `age` int(0) NOT NULL,
  `price_for_training` int(0) NOT NULL,
  `password` varchar(50) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `username` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci NULL DEFAULT NULL,
  PRIMARY KEY (`rid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of private_coach
-- ----------------------------
INSERT INTO `private_coach` VALUES (1, 'Martin', 'Martin', 5, 'male', '242ww@gmail.com', '5039449879', 23, 50, '123', 'Rsil');
INSERT INTO `private_coach` VALUES (2, 'das', 'das', 3, 'female', 'sdw@gmail.com', '503333879', 24, 50, '123', 'Rs');
INSERT INTO `private_coach` VALUES (3, 'Sam', 'Martin', 3, 'male', '1321@qq.com', '5039449875', 26, 60, '123', 'Rsuo');
INSERT INTO `private_coach` VALUES (4, 'Lucy', 'ddd', 6, 'female', 'qa@mail.com', '5039432875', 26, 50, '123', 'Ro');
INSERT INTO `private_coach` VALUES (5, 'dasd', 'Martin', 6, 'female', '666@qq.com', '5045332875', 30, 100, '123', 'Roo');

-- ----------------------------
-- Table structure for section
-- ----------------------------
DROP TABLE IF EXISTS `section`;
CREATE TABLE `section`  (
  `sid` int(0) NOT NULL AUTO_INCREMENT,
  `sname` varchar(20) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `duty` varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci NOT NULL,
  `bid` int(0) NOT NULL,
  PRIMARY KEY (`sid`) USING BTREE,
  INDEX `BID`(`bid`) USING BTREE,
  CONSTRAINT `Section_ibfk_1` FOREIGN KEY (`bid`) REFERENCES `branch` (`bid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 6 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of section
-- ----------------------------
INSERT INTO `section` VALUES (1, 'g5', 'saw', 1);
INSERT INTO `section` VALUES (2, 'dw', 'ws', 4);
INSERT INTO `section` VALUES (3, 'Gym3', 'accounting', 2);
INSERT INTO `section` VALUES (4, 'Gym4', 'Instru', 3);
INSERT INTO `section` VALUES (5, 'Gym5', 'safety', 5);

-- ----------------------------
-- Table structure for train
-- ----------------------------
DROP TABLE IF EXISTS `train`;
CREATE TABLE `train`  (
  `rid` int(0) NOT NULL,
  `mid` int(0) NOT NULL,
  `hour` int(0) NOT NULL,
  PRIMARY KEY (`rid`, `mid`) USING BTREE,
  INDEX `MID`(`mid`) USING BTREE,
  CONSTRAINT `Train_ibfk_1` FOREIGN KEY (`rid`) REFERENCES `private_coach` (`rid`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Train_ibfk_2` FOREIGN KEY (`mid`) REFERENCES `member` (`mid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of train
-- ----------------------------
INSERT INTO `train` VALUES (1, 4, 5);
INSERT INTO `train` VALUES (3, 6, 2);
INSERT INTO `train` VALUES (5, 5, 10);

SET FOREIGN_KEY_CHECKS = 1;
