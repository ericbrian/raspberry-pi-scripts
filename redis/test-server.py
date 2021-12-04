import redis
client = redis.Redis(host='192.168.1.203',port=6379,password='redispass')

client.set('language','Python')
print(client.get('language'))

