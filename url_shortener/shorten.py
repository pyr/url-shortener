import redis
import base64
import hashlib
from .config import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PREFIX, URL_PREFIX


class UrlShortener:
    def __init__(self):
        self.redis = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

    def shortcode(self, url):
        """
        Our main shortening function. The rationale here is that
        we are relying on the fact that for similarly sized inputs
        such as URLs the potential for collision in the 32 last bits
        of the MD5 hash is rather unlikely.

        The following things happen, in order:

        * compute the md5 digest of the given source
        * extract the lower 4 bytes
        * base64 encode the result
        * remove trailing padding if it exists

        Of course, should a collision happen, we will evict the previous
        key.

        """
        md5_digest = hashlib.md5(url.encode()).digest()
        return (
            base64.b64encode(md5_digest[-4:])
            .decode("UTF-8")
            .replace("=", "")
            .replace("/", "_")
        )

    def shorten(self, url):
        """
        The shortening workflow is very minimal. We try to
        set the redis key to the url value. We catch any
        exception in the process to properly report failures
        in the client
        """

        code = self.shortcode(url)

        try:
            self.redis.set(REDIS_PREFIX + code, url)
            return {
                "success": True,
                "url": url,
                "code": code,
                "shorturl": URL_PREFIX + code,
            }
        except:
            return {"success": False}

    def lookup(self, code):
        """
        The same strategy is used for the lookup than for the
        shortening. Here a None reply will imply either an
        error or a wrong code.
        """
        try:
            return self.redis.get(REDIS_PREFIX + code).decode("UTF-8")
        except:
            return None
