
import os
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02709", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get('BenchmarkTest02709', '')

    bar = do_something(param)

    cookie_value = param if param else "No cookie value supplied"
    response.set_cookie('SomeCookie', cookie_value, secure=False, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{escape_html(cookie_value)}' and secure flag set to: false"
    return response

def do_something(param):
    num = 106
    return "This should never happen" if (7 * 42) - num > 200 else param

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
