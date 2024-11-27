
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01862", methods=['GET'])
def benchmark_test():
    response = make_response(render_template("securecookie-00/BenchmarkTest01862.html"))
    user_cookie = "BenchmarkTest01862=whatever; Max-Age=180; Secure; Path={}; Domain={}".format(
        request.path, request.host)
    response.set_cookie("BenchmarkTest01862", "whatever", max_age=180, secure=True, path=request.path, domain=request.host)
    return response

@app.route("/securecookie-00/BenchmarkTest01862", methods=['POST'])
def benchmark_test_post():
    param = "noCookieValueSupplied"
    the_cookies = request.cookies

    if 'BenchmarkTest01862' in the_cookies:
        param = urllib.parse.unquote(the_cookies['BenchmarkTest01862'])

    bar = do_something(param)

    str_param = bar if bar != "" else "No cookie value supplied"
    response = make_response(f"Created cookie: 'SomeCookie': with value: '{str_param}' and secure flag set to: true")
    response.set_cookie("SomeCookie", str_param, secure=True, httponly=True, path=request.path)
    
    return response

def do_something(param):
    return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
