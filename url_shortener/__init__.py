from flask import Flask, json, request, redirect, render_template, make_response
from shorten import UrlShortener
from functools import wraps

app = Flask(__name__)
shrt = UrlShortener()

## template pushing routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/404')
def missing():
    return render_template('missing.html')

@app.route('/400')
def invalid():
    return render_template('invalid')

## short url lookup
@app.route('/<code>')
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
def shorten_url():
    if request.json and 'url' in request.json:
        url = request.json['url']
        res = shrt.shorten(request.json['url'])
        response = make_response(json.dumps(res))
        response.headers['Content-Type'] = 'application/json'
        return response

    elif request.form and 'url' in request.form:
        url = request.form['url']
        res = shrt.shorten(request.form['url'])
        return render_template('result.html', result=res)

    else:
        return redirect('/400')


