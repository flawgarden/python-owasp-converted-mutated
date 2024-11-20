
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00894", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest00894", "")
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    response.headers['X-XSS-Protection'] = "0"
    length = 1
    if bar:
        length = len(bar)
        response.set_data(bar[:length])

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
