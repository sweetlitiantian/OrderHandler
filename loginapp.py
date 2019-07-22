# def login():
#     headers = {"Content-Type": "application/json;charset=UTF-8"}
#     url = 'https://zdapi-test.orderhandler.com/zdapi/user/login'
#     #url = 'https://www.baidu.com'
#     data = {"clientInfo": {"clientid": "11"}, "phone": "15755518373", "smsCode": "3785"}
#     r = requests.post(url=url, data=json.dumps(data), headers=headers)
#     print json.loads(r.text)['token']
#     return json.loads(r.text)['token']

# def getsmscode():
#     headers = {"Content-Type": "application/json;charset=UTF-8"}
#     url = 'https://zdapi-test.orderhandler.com/zdapi/user/get-sms-code'
#     data = {"phone": 15755518373}
#     r = requests.post(url=url, data=json.dumps(data), headers=headers)
#     return r.text


import requests
import json

def login():
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    url = 'https://zdapi-test.orderhandler.com/zdapi/user/login'
    data = {"clientInfo": {"clientid": "11"}, "phone": "15755518373", "smsCode": "1762"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    return r.cookies['token']

def getuser():
    token = login()
    headers = {"Content-Type": "application/json;charset=UTF-8", "token": token}
    url = 'https://zdapi-test.orderhandler.com/zdapi/user/get-user-info'
    data = {}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    print r.text
    return r.text

def loginsale1(self, uri=None, data={}, headers=None):
    r = requests.post(uri, data=data, headers=headers, verify=False)
    file_name = 'd:\\token.txt'
    with open(file_name, 'w') as file_object:
        file_object.write(r.json()['token'])
    return r.json()['token']


