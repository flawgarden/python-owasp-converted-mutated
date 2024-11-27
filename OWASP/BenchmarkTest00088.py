
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00088", methods=['GET', 'POST'])
def benchmark_test_00088():
    if request.method == 'GET':
        resp = make_response(render_template("securecookie-00/BenchmarkTest00088.html"))
        user_cookie = make_response('whatever')
        user_cookie.set_cookie('BenchmarkTest00088', 'whatever', max_age=60*3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        param = 'noCookieValueSupplied'
        the_cookies = request.cookies
        if 'BenchmarkTest00088' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00088'])

        bar = param  # Placeholder for encoding logic

        str_param = param if isinstance(param, str) else ''
        cookie = make_response()
        cookie.set_cookie('SomeCookie', str_param, secure=True, httponly=True, path=request.path)

        return f"Created cookie: 'SomeCookie': with value: '{str_param}' and secure flag set to: true"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
