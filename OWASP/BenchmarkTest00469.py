
from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/xss-00/BenchmarkTest00469", methods=['GET', 'POST'])
def benchmark_test_00469():
    if request.method == 'GET':
        return benchmark_test_00469_post()
    return benchmark_test_00469_post()

def benchmark_test_00469_post():
    response = make_response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = ""
    if request.args:
        param = request.args.get("BenchmarkTest00469", "")

    bar = ""
    num = 106

    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    response.headers["X-XSS-Protection"] = "0"
    response.data = response.response_class.format(bar, ("a", "b"))
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
