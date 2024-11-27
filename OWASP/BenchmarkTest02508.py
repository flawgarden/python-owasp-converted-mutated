
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02508", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        values = request.values.getlist("BenchmarkTest02508")
        param = values[0] if values else ""

        bar = do_something(param)

        str_param = param if isinstance(param, str) else ""

        if str_param == "":
            str_param = "No cookie value supplied"

        response = make_response(render_template("index.html"))

        response.set_cookie("SomeCookie", str_param, secure=True, httponly=True, path=request.path)

        return response, f"Created cookie: 'SomeCookie': with value: '{str_param}' and secure flag set to: true"

def do_something(param):
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
