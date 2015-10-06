#-*-coding=utf-8-*-
''' 各种component初始化的地方 '''

import MySQLdb

def create_local_mysql():
    conn = MySQLdb.connect(host = "127.0.0.1",	#121.40.201.212
                           port = 3808,
                           user = "work", 
                           passwd = "312312", 
                           db = "account_book",
                           charset = 'utf8')
    conn.text_factory = str
    return conn

    