from rediscluster import RedisCluster

startup_nodes = [{"host": "127.0.0.1", "port": "6001"}]


def hello_redis(key,value):
    try:
        r = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

        r.set(key, value)
        print("Key-Value Set in Redis")

        print()
        msg = r.get(key)
        print("Getting Value...")
        print("Value: " + msg + " against Key: " + key)

    except Exception as e:
        print("Error Occurred")
        print(e)


if __name__ == '__main__':
    print("Please provide key")
    key = input()
    print("Please provide value")
    value = input()
    hello_redis(key,value)
