
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01597", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    values = request.args.getlist("BenchmarkTest01597")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    if bar is not None:
        response.set_data(bar)
    return response

class Test:
    def do_something(self, param):
        sbxyz81751 = str(param)
        bar = sbxyz81751 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
