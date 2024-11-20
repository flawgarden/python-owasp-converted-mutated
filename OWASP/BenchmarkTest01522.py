
import os
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01522", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()  # Redirect GET to POST

    response = make_response()

    param = request.args.get("BenchmarkTest01522", "")

    bar = Test().do_something(param)

    cookie = f'SomeCookie={bar}; Secure; HttpOnly; Path={request.path}'
    response.headers.add('Set-Cookie', cookie)

    response.data = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: true"
    return response

class Test:

    def do_something(self, param):
        return self.encode_for_html(param)

    def encode_for_html(self, value):
        return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
