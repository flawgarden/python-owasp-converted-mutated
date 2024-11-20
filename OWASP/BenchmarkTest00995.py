
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00995", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("trustbound-00/BenchmarkTest00995.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00995", "color", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00995' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00995'])

        bar = Test().do_something(request, param)
        request.session[bar] = "10340"

        return f"Item: '{bar}' with value: '10340' saved in session."

class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
