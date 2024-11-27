
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01340", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")
    param = request.args.get("BenchmarkTest01340", "")

    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map36950 = {
            "keyA-36950": "a_Value",
            "keyB-36950": param,
            "keyC": "another_Value"
        }
        bar = map36950.get("keyB-36950")
        bar = map36950.get("keyA-36950")

        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
