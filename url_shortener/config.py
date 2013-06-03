import os
import logging
import logging.config
from logstash_formatter import LogstashFormatter

REDIS_PREFIX = os.getenv("REDIS_PREFIX", "short:")
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
REDIS_DB = int(os.getenv("REDIS_DB", "0"))
URL_PREFIX = os.getenv("URL_PREFIX", "http://exo.po/")
LISTEN_HOST = os.getenv("LISTEN_HOST", "127.0.0.1")
LISTEN_PORT = int(os.getenv("LISTEN_PORT", "8080"))
RIEMANN_HOST = os.getenv("RIEMANN_HOST", "127.0.0.1")
RIEMANN_PORT = int(os.getenv("RIEMANN_PORT", "5555"))


LOG_FILE_PATH = os.getenv('LOG_FILE_PATH')
LOG_LEVEL = os.getenv('LOG_LEVEL', 'DEBUG')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'logstash': {
            '()': LogstashFormatter,
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s:%(name)s: %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': LOG_LEVEL,
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
        'logstash': {
            'level': LOG_LEVEL,
            'class': 'logging.NullHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'root': {
        'handlers': ['console', 'logstash'],
        'level': 'DEBUG',
        'propagate': False,
    },
    'loggers': {
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'url_shortener': {
            'handlers': ['console', 'logstash'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}
if LOG_FILE_PATH:
    LOGGING['handlers']['logstash'] = {
        'level': 'DEBUG',
        'class': 'logging.handlers.WatchedFileHandler',
        'formatter': 'logstash',
        'filename': LOG_FILE_PATH,
    }
    LOGGING['handlers']['console'] = {
        'class': 'logging.NullHandler',
    }
logging.config.dictConfig(LOGGING)
