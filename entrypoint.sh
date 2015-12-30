#!/bin/sh

trap cleanup 1 2 3 6

cleanup() {
  echo -n "Caught signal! Shutting down ... "
  killall gunicorn
  echo "OK"
  exit 1
}

touch /var/log/gunicorn.log

gunicorn -D -w 8 -b ${LISTEN_HOST}:${LISTEN_PORT} \
  --log-file=/var/log/gunicorn.log \
  --log-level=info \
  url_shortener:app

tail -f /var/log/gunicorn.log
