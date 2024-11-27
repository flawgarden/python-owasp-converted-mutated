
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02065", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    
    param = ""
    if 'BenchmarkTest02065' in request.headers:
        param = request.headers['BenchmarkTest02065']

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    if not param:
        param = "No cookie value supplied"

    response.set_cookie('SomeCookie', param, secure=True, httponly=True, path=request.path)
    
    response.data = f"Created cookie: 'SomeCookie': with value: '{escape_html(param)}' and secure flag set to: true"
    
    return response

def do_something(param):
    num = 106
    return "This_should_always_happen" if (7 * 18) + num > 200 else param

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
