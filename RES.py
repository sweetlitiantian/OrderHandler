import redis
# print r.get('zd_sms_15755518373')

class RES():
    def ConnectionRedis(self,sql):
        # r = redis.Redis(host='192.168.1.22', port=6379,decode_responses=True)
        r = redis.Redis(host='192.168.2.23', port=6379,decode_responses=True)
        # r = redis.Redis(host='47.100.236.151', port=6373,decode_responses=True)
        code = r.get(sql)
        return code
if __name__=='__main__':
    print RES().ConnectionRedis('zd_sms_15755518373')