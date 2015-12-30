FROM prologic/python-runtime:2.7-onbuild

ENTRYPOINT ["/entrypoint.sh"]
CMD []

EXPOSE 80

ENV REDIS_HOST="redis"
ENV LISTEN_HOST="0.0.0.0"
ENV LISTEN_PORT="80"
ENV URL_PREFIX=""

COPY entrypoint.sh /entrypoint.sh
