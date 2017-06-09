import redis

POOL = redis.ConnectionPool(host='localhost', port=6379, password="password123", db=0)
TEST_POOL = redis.ConnectionPool(host='localhost', port=6379, password="password123", db=1)  # For test database


def get_variable(key, pool=POOL):
    """:return variable of key"""
    my_server = redis.Redis(connection_pool=pool)
    return my_server.get(key)


def set_variable(key, value, pool=POOL):
    """set variable by key"""
    my_server = redis.Redis(connection_pool=pool)
    return my_server.set(key, value)


def delete_variable(key, pool=POOL):
    """delete varable by key"""
    my_server = redis.Redis(connection_pool=pool)
    return my_server.delete(key)


def increment_or_initialize(key, pool=POOL):
    """increment key if it not exist set key with default variable 1,
    note that this operation is atomic according to redis docs"""
    my_server = redis.Redis(connection_pool=pool)
    return my_server.incr(key, amount=1)


def flush_all(pool=TEST_POOL):
    """flush all keys in database"""
    my_server = redis.Redis(connection_pool=pool)
    return my_server.flushall()
