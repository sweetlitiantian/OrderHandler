# -*- coding: utf-8 -*-
import sys
from urllib3.exceptions import InsecureRequestWarning
import hashlib

if sys.getdefaultencoding() != 'UTF-8':
    reload(sys)
    sys.setdefaultencoding('UTF-8')
print sys.getdefaultencoding()
import json
# FILE_OBJECT = open('url.txt','r', encoding='UTF-8')
import requests
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import logging
# pymysql.install_as_MySQLdb()
# import pymysql as MySQLdb
#
# import MySQLdb

# db = MySQLdb.connect(host='192.168.1.223', port=3306, passwd='123456', user='root')

class ValueErro(object):
    pass


class OrderHandlerKeywords(object):

    def init(self):
        pass

    def op_login(self, uri=None, data={}, headers=None):
        """ OP登录接口  传入后返回 ${UserToken}
        ``--url--：``  环境登录地址
        ``--data--：``    传入数据
        ``--headers--：``      报文头
        """
        logging.info("uri:" + uri)
        r = requests.post(uri, data=data, headers=headers, verify=False)
        if (r.status_code == 200):
            logging.info('status=' + str(r.status_code))
        else:
            raise RuntimeError('接口状态错误,状态码为' + r.status_code)
        logging.info("result:" + r.text)
        result = r.text
        usertToken = result.split("userToken\":\"")[1]
        usertToken = usertToken.split("\"")[0]
        logging.info("usertToken:" + usertToken)
        return usertToken

    def post_Response(self, url=None, data1={}, headers=None):

        """执行Post请求后获得response
        `--url--：``  环境登录地址
        `--data--：``    传入数据
        `--headers--：``      报文头
        """
        response = requests.post(url, data=data1, headers=headers, verify=False)
        if response.status_code == 200:
            res = response.text
            logging.info(res)
            logging.info('status=' + str(response.status_code))
        else:
            raise RuntimeError('接口状态错误,状态码为' + response.status_code)
        return res

    def check_ResponseKey(self, crurl=None, crdata={}, headers=None, list=[]):
        """ 检查response中是否含有List中的字段
        ``--url--：``  环境登录地址
        ``--data--：``    传入数据
        ``--headers--：``      报文头
        ``--list--：``  检查字段集合
        """
        rr = self.post_Response(crurl, data1=crdata, headers=headers)
        for key in list:
            if rr.__contains__(key):
                logging.info("字段检查通过:" + key)
            else:
                raise RuntimeError('字段检查失败:' + key)

    def wgpost(self, url=None, data={}, headers=None, cookies=None):
        logging.info(url)
        # data = json.dumps(data,ensure_ascii=False)
        data = data.encode('unicode_escape')
        if cookies == "None":
            response = requests.post(url, data=data, headers=headers, verify=False)
            logging.info(response.text)
        else:
            cookie = dict(SESSION=cookies)
            logging.info(cookie)
            response = requests.post(url, data=data, cookies=cookie, headers=headers, verify=False)
            logging.info("2252" + response.text)
        res = response.text
        if response.status_code == 200:
            logging.info('status=' + str(response.status_code))
        else:
            raise RuntimeError('接口状态错误,状态码为' + response.status_code)
        return res

    def wgpost1(self, url=None, data={}, headers=None, cookies=None):
        logging.info(url)
        data = data.encode('unicode_escape')
        if cookies == "None":
            response = requests.post(url, data=data, headers=headers, verify=False)
            logging.info(response.text)
        else:
            msg = eval(cookies)
            _cookies = 'token=' + msg[2] + ';saleMobile=' + msg[1] + ';saleId=' + msg[0]
            headers = {
                'Content-Type': 'application/json;charset=UTF-8',
                'Cookie': _cookies
            }
            datas = str(data)

            response = requests.post(url, data=datas, headers=headers, verify=False)

            logging.info("868686" + response.text)
        res = response.text
        if response.status_code == 200:
            logging.info('status=' + str(response.status_code))
        else:
            raise RuntimeError('接口状态错误,状态码为' + response.status_code)
        return res

    def wgcheck_reponseKey(self, url=None, data={}, cookies=None, headers=None, list=[]):
        headers = {"Content-Type": "application/json;charset=UTF-8", "appVersion": "1.3.0"}
        rr = self.wgpost(url, data=data, cookies=cookies, headers=headers)
        for key in list:
            if rr.__contains__(key):
                logging.info("test字段检查通过:" + key)
            else:
                raise RuntimeError('字段检查失败:' + key)

        file_name = 'd:\\token.txt'
        with open(file_name, 'w') as file_object:
            file_object.write(rr.json()['token'])
        logging.info("---------------rt------")
        return rr.json()['token']


    def wgcheck_reponseKey2(self, url=None, data={}, cookies=None, headers=None, list=[]):

        f = open('d:\\token.txt', 'r')
        f_read = f.read()
        print(f_read)
        token = f_read
        headers = {"Content-Type": "application/json;charset=UTF-8", "token": token,"appVersion": "1.3.0"}

        rr = self.wgpost1(url, data=data, cookies=cookies, headers=headers)

        for key in list:
            if rr.__contains__(key):
                logging.info("字段检查通过:" + key)
            else:
                raise RuntimeError('字段检查失败:' + key)

    def get_Url(self, uri=None, url=None, jsondata={}):
        """取得get方法中url拼接的参数
        ''--json_data--''  接口所传入参
        """
        # jsondata = urllib.quote_plus(jsondata)
        logging.info('%s%s%s' % (uri, url, jsondata))
        return '%s%s%s' % (uri, url, jsondata)
        # url = uri+url+"?"
        # return url

    def get_Response(self, url=None, cookies=None):
        """使用get请求
         ``--url--：``  环境登录地址

         """
        if cookies is None:
            rr = requests.get(url)
        else:
            cookie = dict(SESSION=cookies)
            rr = requests.get(url, cookies=cookie)
            logging.info(rr.status_code)
        if rr.status_code == 200:
            res = rr.text
            logging.info(res)
        else:
            raise RuntimeError('接口状态错误,状态码为' + str(rr.status_code))
        return res

    def getck_ResponseKey(self, url=None, cookies=None, list=[]):
        """检查response中是否含有list中的字段
        ''--urll--''  接口url
        ``--list--：``  检查字段集合
        """
        logging.info("777777")
        rr = self.get_Response(url, cookies, )
        logging.info(rr)
        logging.info("sessionid:" + cookies)
        for key in list:
            if rr.__contains__(key):
                logging.info("字段检查通过:" + key)
            else:
                raise RuntimeError('字段检查失败:' + key)

    def login(self, uri=None, data={}, headers=None):
        """ OP登录接口  传入后返回 ${UserToken}
        ``--url--：``  环境登录地址
        ``--data--：``    传入数据
        ``--headers--：``      报文头

        """
        # uri = '%s%s%s' % (uri, url, jsondata)

        r = requests.post(uri, data=data, headers=headers, verify=False)
        logging.info(r.cookies.values())

        logging.info("----------------------")
        logging.info("1111" + r.cookies['SESSION'])

        return r.cookies['SESSION']

    def login2(self, uri=None, data={}, headers=None):

        headers = {"Content-Type": "application/json;charset=UTF-8", "appVersion": "1.3.0"}
        r = requests.post(uri, data=data, headers=headers, verify=False)
        file_name = 'd:\\token.txt'
        with open(file_name, 'w') as file_object:
            file_object.write(r.json()['token'])
        logging.info("---------------------")
        return r.json()['token']


    def loginsale(self, uri=None, data={}, headers=None):
        """ OP登录接口  传入后返回 ${UserToken}
        ``--url--：``  环境登录地址
        ``--data--：``    传入数据
        ``--headers--：``      报文头
        """
        # uri = '%s%s%s' % (uri, url, jsondata)
        r = requests.post(uri, data=data, headers=headers, verify=False)

        logging.info('cookies:' + str(r.cookies.values()))

        logging.info("---------------------")

        return str(r.cookies.values())

    def userId(self, url=None, data={}, headers=None, cookies=None):

        text = self.wgpost(url, data=data, headers=headers, cookies=cookies)
        # userToken\":\"  id\":\"   .split(":[{")[-1]
        # id = text.split("\"id\":")[1]
        id = text.split(",\"userName")[0].split(":[{")[-1].split("\"id\":")[1]
        id = [int(id)].__str__()
        return id

    def roleId(self, url=None, data={}, headers=None, cookies=None):

        text = self.wgpost(url, data=data, headers=headers, cookies=cookies)
        id = text.split(",\"status")[0].split(":[{")[-1].split("\"id\":")[1]
        id = [int(id)].__str__()
        logging.info("获取roleid:" + id)
        return id

    def commodityId(self, url=None, data={}, headers=None, cookies=None):

        text = self.wgpost(url, data=data, headers=headers, cookies=cookies)
        id = text.split(",\"commodityName")[0].split(":[{")[-1].split("\"id\":")[1]
        id = [int(id)].__str__()
        logging.info("获取id:" + id)
        return id[1:len(id) - 1]


    #
    # def mysql(self, sql):
    #     cursor = db.cursor()
    #     cursor.execute(sql)
    #     data = cursor.fetchall()
    #     # code =data[len(data)-1][0]
    #     code = data[0][0]
    #     return code

    # def getcode(self,url=None,data={},headers=None,cookies=None):
    #   text = text


if __name__ == "__main__":
    baseUrl = 'https://api-test.orderhandler.com'

    order = OrderHandlerKeywords()
    # cookies = {'cookie': 'SESSION=MjY1ZjE5YTgtNTY4Yy00NGMwLTlmNTItYzc3MWQxODk3YTA2'

    # cookie = order.get_Response('http://101.132.141.172:10002/auth/login',
    #                             '?userName=admin&password=1&registerFrom=admin')

    # cookie=order.login("http://101.132.141.172:10002/auth/login",{"userName":"admin","password":"1","registerFrom":"admin"},"application/json;charset=UTF-8")
    # http: // api - dev.orderhandler.com /        http://101.132.141.172:10002/
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    orders = order.mysql(
        'SELECT sms_code FROM salelogin.t_sale_login_verified where mobile=18296637285 ORDER BY send_time DESC   LIMIT 1')
    print(orders)

    # login = order.login(baseUrl + '/admin/auth/login', '{"userName":"admin","password":"123","registerFrom":"admin"}')
    # print login
    # url ='http://192.168.1.111:10016/admin/login'
    # a =order.userId(self,url=None, data={}, headers=None, cookies=None)
