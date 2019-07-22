# -*- coding: utf-8 -*-
import requests
import logging
import sys
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
if sys.getdefaultencoding() != 'UTF-8':
    reload(sys)
    sys.setdefaultencoding('UTF-8')

# print (sys.getdefaultencoding())


class ValueErro(object):
    pass


class appToken():

  def init(self):
        pass

  def wg(self, url=None, data={}, headers=None, cookies=None):
    logging.info(url)
    # data = json.dumps(data,ensure_ascii=False)
    data = data.encode('unicode_escape')
    if cookies == "None":
        response = requests.post(url, data=data, headers=headers, verify=False)
    else:
        cookie = dict(SESSION=cookies)
        response = requests.post(url, data=data, cookies=cookie, headers=headers, verify=False)
    res = response.text
    if response.status_code == 200:
        logging.info('status=' + str(response.status_code))
    else:
        raise RuntimeError('接口状态错误,状态码为' + response.status_code)
    return res


  def wgcheck_reponseKeytest(self, url=None, data={}, headers=None, list=[]):
    f = open('d:\\token.txt', 'r')
    f_read = f.read()
    print(f_read)
    token = f_read

    headers = {"Content-Type": "application/json;charset=UTF-8", "token": token}
    rr = self.wg(url, data=data, cookies=None, headers=headers)
    for key in list:
        if rr.__contains__(key):
            logging.info("字段检查通过:" + key)
        else:
            raise RuntimeError('字段检查失败:' + key)


  def getToken(self, uri=None, data={}, headers=None):
    r = requests.post(uri, data=data, headers=headers, verify=False)
    file_name = 'd:\\token.txt'
    with open(file_name, 'w') as file_object:
        file_object.write(r.json()['token'])
    return r.json()['token']