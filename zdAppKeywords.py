import logging
import requests
class zdAppKeywords():
     def __init__(self):
        pass

     def wgpost(self, url=None, data={}, headers=None, cookies=None):
         logging.info(url)
         # data = json.dumps(data,ensure_ascii=False)
         data = data.encode('unicode_escape')

         if cookies == "None":
             response = requests.post(url, data=data, headers=headers, verify=False)
             logging.info(response.text)
         else:
             cookie = dict(SESSION=cookies)
             response = requests.post(url, data=data, cookies=cookie, headers=headers, verify=False)
         res = response.text
         if response.status_code == 200:
             logging.info('status=' + str(response.status_code))
         else:
             raise RuntimeError('接口状态错误,状态码为' + response.status_code)
         return res

     def wgcheck_reponseKey(self, url=None, data={}, cookies=None, headers=None, list=[]):
        headers = {"Content-Type": "application/json;charset=UTF-8", "token": cookies}
        logging.info(headers)
        rr = self.wgpost(url, data=data, cookies=None, headers=headers)
        for key in list:
            if rr.__contains__(key):
                logging.info("test字段检查通过:" + key)
            else:
                raise RuntimeError('字段检查失败:' + key)