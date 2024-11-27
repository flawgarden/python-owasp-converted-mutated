
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02136", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = request.args.get("BenchmarkTest02136", "")
    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    if bar is not None:
        response.data = bar.encode('utf-8')
        response.content_length = len(response.data)
    
    return response

def do_something(param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
