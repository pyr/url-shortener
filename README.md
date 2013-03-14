url-shortener: demo URL shortening service in python
====================================================

A demo application for a very simple URL shortening service

The app relies on:

* [flask](http://flask.pocoo.org): A python micro web framework
* [bootstrap](http://twitter.github.com/bootstrap): A CSS & JS framework

## Requirements

```shell
easy_install pip
pip install -e .
```

## Configuration

Configuration happens in `config.py`, the following variables need
to be set:

* `REDIS_HOST`: where redis lives
* `REDIS_PORT`: redis port
* `REDIS_PREFIX`: key prefix for short urls
* `REDIS_DB`: redis database index (usually 0)
* `URL_PREFIX`: URL scheme for your short url host

## Running

Once installed, `url-shortener` launches a server on port 8000

## Deploying

This can be directly deployed with gunicorn
