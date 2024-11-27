
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

@app.route("/securecookie-00/BenchmarkTest01282", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get('BenchmarkTest01282', "")

    bar = Test().do_something(param)

    cookie = make_response()
    cookie.set_cookie('SomeCookie', bar, httponly=True, path=request.path)

    response.headers.add("Set-Cookie", cookie.headers["Set-Cookie"])
    response.data = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: false"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
