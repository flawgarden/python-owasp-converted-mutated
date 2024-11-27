
import base64
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01062", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()

    param = request.headers.get("BenchmarkTest01062", "")
    param = base64.urlsafe_b64decode(param).decode('utf-8') if param else ""

    bar = Test().do_something(param)

    str_param = param if param else "No cookie value supplied"
    cookie = make_response()
    cookie.set_cookie("SomeCookie", str_param, secure=True, httponly=True, path=request.path)

    response.set_cookie("SomeCookie", str_param, secure=True, httponly=True, path=request.path)
    response.data = f"Created cookie: 'SomeCookie': with value: '{str_param}' and secure flag set to: true"
    return response

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode('utf-8'))).decode('utf-8')
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
