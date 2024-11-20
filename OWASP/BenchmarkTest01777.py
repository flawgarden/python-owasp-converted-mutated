
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01777", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return do_post(request)

def do_post(request):
    response = Response()
    response.content_type = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest01777")

    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    length = 1
    if bar is not None:
        length = len(bar)
        response.data = bar[:length]
    return response

class Test:
    def do_something(self, request, param):
        bar = None
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
