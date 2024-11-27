
from flask import Flask, request, make_response
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02427", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest02427", "")

    bar = do_something(param)

    if bar == "":
        bar = "No cookie value supplied"
    cookie = make_response()
    cookie.set_cookie("SomeCookie", bar, secure=False, httponly=True, path=request.path)
    
    response.set_cookie("SomeCookie", bar, secure=False, httponly=True, path=request.path)
    response.data = f"Created cookie: 'SomeCookie': with value: '{escape_html(bar)}' and secure flag set to: false"
    return response

def do_something(param):
    if param is not None and len(param) > 1:
        return param[:-1]
    return param

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
