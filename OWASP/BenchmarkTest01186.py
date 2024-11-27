
import urllib.parse
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01186", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = ""
    headers = request.headers.getlist("BenchmarkTest01186")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cookie = "SomeCookie"
    cookie_value = bar if bar else "No cookie value supplied"
    response.set_cookie(cookie, cookie_value, httponly=True, secure=False, path=request.path)

    response.data = f"Created cookie: '{cookie}': with value: '{cookie_value}' and secure flag set to: false"
    return response

class Test:
    def do_something(self, param):
        return self.html_escape(param)

    def html_escape(self, param):
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
