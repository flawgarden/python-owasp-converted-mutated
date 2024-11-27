
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01863", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("securecookie-00/BenchmarkTest01863.html"))
        user_cookie = ('BenchmarkTest01863', 'whatever', 60 * 3, True, request.path, request.host.split(':')[0])
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=user_cookie[3], path=user_cookie[4], domain=user_cookie[5])
        return response
    
    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies

        if 'BenchmarkTest01863' in cookies:
            param = unquote(cookies['BenchmarkTest01863'])

        bar = do_something(param)

        str_param = param if isinstance(param, str) else ""
        if str_param == "":
            str_param = "No cookie value supplied"
        
        response = make_response(f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: true")
        response.set_cookie('SomeCookie', str_param, secure=True, httponly=True, path=request.path)
        return response


def do_something(param):
    return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")  # Simple escaping for HTML.

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
