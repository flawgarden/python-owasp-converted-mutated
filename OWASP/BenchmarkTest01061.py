
from flask import Flask, request, make_response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01061", methods=['GET', 'POST'])
def benchmark_test_01061():
    if request.method == 'GET':
        return benchmark_test_01061_post()

    return benchmark_test_01061_post()

def benchmark_test_01061_post():
    param = request.headers.get("BenchmarkTest01061", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cookie = make_response(render_template("index.html"))
    cookie.set_cookie("SomeCookie", bar, secure=False, httponly=True, path=request.path)

    response_message = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: false"
    return response_message

class Test:

    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            sbxyz37461 = list(param)
            sbxyz37461[-1] = 'Z'
            bar = ''.join(sbxyz37461)
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
