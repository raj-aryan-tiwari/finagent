import redis

def test_redis():
    r = redis.Redis(host="localhost", port=6379)
    r.set("finagent_test", "hello from FinAgent!")
    value = r.get("finagent_test").decode()
    print(f"Redis working: {value}")

test_redis()