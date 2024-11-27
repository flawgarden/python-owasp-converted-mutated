
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest01521", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = request.args.get("BenchmarkTest01521", "")
    bar = Test().do_something(param)

    cookie = f'SomeCookie={bar}; HttpOnly; Path={request.path}'
    response.set_cookie('SomeCookie', bar, httponly=True, secure=False, path=request.path)

    response.data = ("Created cookie: 'SomeCookie': with value: '" +
                     bar + "' and secure flag set to: false").encode('utf-8')

    return response


class Test:

    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
