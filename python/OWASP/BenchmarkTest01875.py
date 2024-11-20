
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01875", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("trustbound-01/BenchmarkTest01875.html"))
        user_cookie = os.urandom(16).hex()
        resp.set_cookie("BenchmarkTest01875", "color", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest01875" in the_cookies:
            param = the_cookies["BenchmarkTest01875"]
        
        bar = do_something(request, param)
        request.session[bar] = "10340"

        return f"Item: '{bar}' with value: '10340' saved in session."

def do_something(request, param):
    bar = param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
