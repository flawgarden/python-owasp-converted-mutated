
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/xss-01/BenchmarkTest00881", methods=['GET', 'POST'])
def benchmark_test_00881():
    if request.method == 'GET':
        return benchmark_test_00881_post()
    return benchmark_test_00881_post()

def benchmark_test_00881_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest00881")

    # Simple ? condition that assigns constant to bar on true condition
    num = 106

    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
