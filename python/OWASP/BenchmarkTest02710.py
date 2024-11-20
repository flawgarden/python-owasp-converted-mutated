
from flask import Flask, request, make_response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest02710", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest02710", "")
    bar = do_something(param)

    str_param = param if isinstance(param, str) else "No cookie value supplied"
    cookie = make_response(f"Created cookie: 'SomeCookie': with value: '{html.escape(str_param)}' and secure flag set to: false")
    cookie.set_cookie("SomeCookie", str_param, httponly=True, path=request.path)

    return cookie


def do_something(param):
    return html.escape(param)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
