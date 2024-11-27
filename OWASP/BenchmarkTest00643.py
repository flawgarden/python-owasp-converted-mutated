
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00643", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00643", "")
    bar = param + "_SafeStuff"

    response = app.response_class(
        response=bar,
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
