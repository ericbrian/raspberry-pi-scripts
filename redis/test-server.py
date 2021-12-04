import redis
client = redis.Redis(host='[hostname here]', port=6379, password='[password here]')

client.set('language','Python')
print(client.get('language'))

