import os

REDIS_PREFIX = os.getenv("REDIS_PREFIX", "short:")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
URL_PREFIX = os.getenv("URL_PREFIX", "http://exo.po/")
LISTEN_HOST = os.getenv("LISTEN_HOST", "127.0.0.1")
LISTEN_PORT = int(os.getenv("LISTEN_PORT", "8080"))
