
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02507", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    values = request.args.getlist("BenchmarkTest02507") if request.method == 'GET' else request.form.getlist("BenchmarkTest02507")
    param = values[0] if values else ""

    bar = do_something(param)

    cookie_value = param if param else "No cookie value supplied"
    response.set_cookie("SomeCookie", cookie_value, secure=False, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{escape(cookie_value)}' and secure flag set to: false"
    return response

def do_something(param):
    num = 106
    return param if (7 * 42) - num <= 200 else "This should never happen"

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
