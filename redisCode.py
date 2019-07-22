import redis
import hashlib
from common.configHttp import RunMain

def get_redis(phone):

    headers = {'Content-Type': 'application/json'}
    data = {"phone": phone}
    result= RunMain().run_main('post', 'https://zdapi-test.orderhandler.com/zdapi/user/get-sms-code', data, headers)
    conn = redis.Redis(host='192.168.2.23', port=6379)
    code=str(conn.get("zd_sms_"+phone),encoding='utf-8')
    return code

def get_md5Code(s):
  md5=hashlib.md5()
  b=s.encode(encoding='utf-8')
  md5.update(b)
  code=md5.hexdigest()
  return code

def de_md5Code(md5Code):
    for i in range(0,10000):
     num =format(i)
     code=get_md5Code(num)
     if(code==md5Code):
      return num
    else:
     return "0000"

def format(a):
    vcode=str(a)
    while len(vcode)<4:
        vcode="0"+vcode
    return vcode

if __name__ == '__main__':
    print(de_md5Code(get_redis('18721110242')))
