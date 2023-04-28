import redis

# Connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0)

# Set a key-value pair in Redis
r.set('example_key', 'example_value')
r.set('0', '1')

# Get the value of a key in Redis
value = r.get('example_key')
test = r.get('0')

print(test.decode('utf-8'))  # Output: example_value
