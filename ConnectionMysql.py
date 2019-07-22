# -*- coding: UTF-8 -*-
import sys


from urllib3.exceptions import InsecureRequestWarning
#
# if sys.getdefaultencoding() != 'UTF-8':
#     reload(sys)
#     sys.setdefaultencoding('UTF-8')

# print sys.getdefaultencoding()

if sys.getdefaultencoding() != 'gbk':
  reload(sys)
sys.setdefaultencoding('gbk')
default_encoding = sys.getdefaultencoding()
# print(results[0].decode('gbk','ignore').encode('utf-8'))


import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb
db = MySQLdb.connect(host='192.168.1.223', port=3306, passwd='123456', user='root')

def ConnectionMysql(sql):
    cursor = db.cursor()
    cursor.execute("select sms_code from salelogin.t_sale_login_verified where mobile='15755518373' ORDER BY send_time DESC LIMIT 1")
    data = cursor.fetchall()
    code = data[0][0]
    return code




