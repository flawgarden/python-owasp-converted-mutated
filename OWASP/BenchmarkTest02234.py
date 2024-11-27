
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02234", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    map = request.args.to_dict()
    if map:
        values = map.get("BenchmarkTest02234")
        if values is not None:
            param = values

    bar = do_something(param)

    response = Response()
    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    return response

def do_something(param):
    sbxyz86132 = str(param)
    bar = sbxyz86132 + "_SafeStuff"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
