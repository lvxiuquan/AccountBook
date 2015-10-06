#-*-coding=utf-8-*-
'''
相关的数据库表结构
'''


account_info = '''
    CREATE TABLE `account_info` (
      `ID` int(11) NOT NULL AUTO_INCREMENT,
      `Description` varchar(64) NOT NULL COMMENT '消费内容',
      `Amount` float(10,0) NOT NULL COMMENT '消费金额',
      `Time` datetime NOT NULL COMMENT '消费日期',
      `UserLv` float(10,0) DEFAULT '0',
      `UserYu` float(10,0) DEFAULT '0',
      `UserXu` float(10,0) DEFAULT '0',
      `Operator` int(8) NOT NULL COMMENT '操作人',
      `EditDate` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
      PRIMARY KEY (`ID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''

account_present = '''
    CREATE TABLE `account_present` (
      `ID` int(11) NOT NULL AUTO_INCREMENT,
      `UserID` int(8) NOT NULL,
      `Amount` float(10,0) NOT NULL,
      PRIMARY KEY (`ID`),
      KEY `account_present_ibfk_1` (`UserID`),
      FOREIGN KEY (`UserID`) REFERENCES `auth_user` (`id`) ON DELETE NO ACTION ON UPDATE CASCADE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''
