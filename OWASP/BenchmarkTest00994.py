
import os
from flask import Flask, request, render_template, make_response, escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00994", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("trustbound-00/BenchmarkTest00994.html"))
        user_cookie = ('BenchmarkTest00994', 'my_user_id', 60 * 3)  # Store cookie for 3 minutes
        resp.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host)
        return resp

    elif request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if "BenchmarkTest00994" in cookies:
            param = cookies.get("BenchmarkTest00994")

        bar = Test().do_something(request, param)
        request.environ['SESSION']['userid'] = bar

        return f"Item: 'userid' with value: '{escape(bar)}' saved in session."

class Test:
    def do_something(self, request, param):
        bar = escape(param)
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
