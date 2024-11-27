
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest02006", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    for name in request.headers:
        if name in common_headers():
            continue

        param = name
        break

    bar = do_something(request, param)

    str_value = param if isinstance(param, str) else "No cookie value supplied"
    cookie = f'SomeCookie={str_value}; Path={request.path}; Secure; HttpOnly'
    
    response.set_cookie("SomeCookie", str_value, secure=True, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{escape(str_value)}' and secure flag set to: true"
    response.content_type = "text/html;charset=UTF-8"
    return response


def do_something(request, param):
    return f"{param}_SafeStuff"


def common_headers():
    return set(['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 
                'Authorization', 'Cache-Control', 'Connection', 'Cookie', 
                'Content-Length', 'Content-Type', 'DNT', 'Host', 'If-Modified-Since', 
                'If-None-Match', 'Origin', 'Referer', 'User-Agent', 'Upgrade-Insecure-Requests'])


def escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
