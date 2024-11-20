
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        bar = param
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.route("/securecookie-00/BenchmarkTest00977", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("securecookie-00/BenchmarkTest00977.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00977", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest00977", "whatever", max_age=60 * 3, secure=True, path=request.path)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00977" in the_cookies:
            param = the_cookies["BenchmarkTest00977"]

        bar = Test().do_something(param)

        cookie_value = param if param else "No cookie value supplied"
        response = make_response(f"Created cookie: 'SomeCookie': with value: '{cookie_value}' and secure flag set to: false")

        response.set_cookie("SomeCookie", cookie_value, secure=False, httponly=True, path=request.path)
        return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
