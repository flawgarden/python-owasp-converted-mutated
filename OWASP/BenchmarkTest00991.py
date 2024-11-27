
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest00991", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("trustbound-00/BenchmarkTest00991.html"))
        user_cookie = ('BenchmarkTest00991', 'color')
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00991' in the_cookies:
            param = the_cookies['BenchmarkTest00991']

        bar = Test().do_something(param)

        request.session[bar] = "10340"

        return f"Item: '{bar}' with value: 10340 saved in session."

class Test:
    def do_something(self, param):
        bar = self.html_escape(param)
        return bar

    def html_escape(self, text):
        return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
