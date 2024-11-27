
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02224", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")
    map_data = request.args.to_dict()
    param = ""
    if map_data:
        values = map_data.get("BenchmarkTest02224")
        if values:
            param = values

    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = f"Formatted like: a and {bar}."
    return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
