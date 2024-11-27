
from flask import Flask, request, make_response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest01359", methods=['GET', 'POST'])
def benchmark_test_01359():
    if request.method == 'GET':
        return benchmark_test_01359_post()
    return benchmark_test_01359_post()

def benchmark_test_01359_post():
    response = make_response()
    param = request.args.get('BenchmarkTest01359', '')

    bar = Test().do_something(param)

    if bar == '':
        bar = "No cookie value supplied"

    cookie = make_response(f"Created cookie: 'SomeCookie': with value: '{html.escape(bar)}' and secure flag set to: true")
    cookie.set_cookie('SomeCookie', bar, secure=True, httponly=True, path=request.path)

    return cookie

class Test:
    def do_something(self, param):
        return html.escape(param)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
