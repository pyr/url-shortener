import logging
from flask import Flask, json, request, redirect, render_template, make_response
from shorten import UrlShortener
from functools import wraps
from bernhard import Client
from riemann_wrapper import riemann_wrapper
import urlparse

app = Flask(__name__)
shrt = UrlShortener()
logger = logging.getLogger()

logger.info("starting up")
try:
    riemann_client = Client(host=config.RIEMANN_HOST,
                            port=config.RIEMANN_PORT)
    riemann_client.send({'metric': 1, 
                         'service': 
                         'url-shortener.startup', 
                         'ttl': 3600})
except:
    riemann_client=None

wrap_riemann = riemann_wrapper(client=riemann_client, prefix='url-shortener.')

## template pushing routes
@app.route('/')
@wrap_riemann('home')
def index():
    return render_template('index.html')

@app.route('/404')
@wrap_riemann('missing', tags=['http_404'])
def missing():
    return render_template('missing.html')

@app.route('/400')
@wrap_riemann('invalid', tags=['http_400'])
def invalid():
    return render_template('invalid')

## short url lookup
@app.route('/<code>')
@wrap_riemann('lookup')
def lookup(code):
    url = shrt.lookup(code)
    if not url:
        return redirect('/404')
    else:
        return redirect(url)
    
## short url generation
##
## If JSON is fed, we shorten and reply in JSON as well
## If a Form is posted we reply in HTML
## Otherwise we redirect to a failure page
@app.route('/', methods=['POST'])
@wrap_riemann('creation')
def shorten_url():
    if request.json and 'url' in request.json:
        u = urlparse.urlparse(request.json['url'])
        if u.netloc == '':
            url = 'http://' + request.json['url']
        else:
            url = request.json['url']

        if 'surl' in request.json.keys():
            surl = request.form['surl'].split()[0].lower()
            res = shrt.shorten(url, surl)
        else:
            res = shrt.shorten(url)

        logger.debug("shortened %s to %s" % (url, res))
        response = make_response(json.dumps(res))
        response.headers['Content-Type'] = 'application/json'
        return response

    elif request.form and 'url' in request.form:
        u = urlparse.urlparse(request.form['url'])
        if u.netloc == '':
            url = 'http://' + request.form['url']
        else:
            url = request.form['url']

        if request.form['surl'] == 'Optional, ShortURL' or request.form['surl'] == '':
            surl = None
        else:
            surl = request.form['surl'].split()[0].lower()

        res = shrt.shorten(url, surl)
        logger.debug("shortened %s to %s" % (url, res))
        return render_template('result.html', result=res)

    else:
        logger.info("invalid shorten request")
        return redirect('/400')
