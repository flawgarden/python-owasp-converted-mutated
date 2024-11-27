
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00651", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'

    param = request.args.get("BenchmarkTest00651", "")
    bar = ""

    # Simple if statement that assigns param to bar on true condition
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar is not None:
        length = len(bar)
        response.data = bar[:length]

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
