
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02483", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return do_post(request)

def do_post(request):
    response = Response()
    response.content_type = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest02483")
    param = values[0] if values else ""

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
