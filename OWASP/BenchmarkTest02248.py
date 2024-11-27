
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02248", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    if request.args:
        param = request.args.get("BenchmarkTest02248", "")

    bar = do_something(param)

    if not bar:
        bar = "No cookie value supplied"

    cookie = make_response(f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: true")
    cookie.set_cookie("SomeCookie", bar, secure=True, httponly=True, path=request.path)

    return cookie

def do_something(param):
    bar = ""
    if param:
        bar = param.split(" ")[0]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

if __name__ == "__main__":
    app.run(host='0.0.0.0')
