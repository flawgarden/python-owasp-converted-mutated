
from flask import Flask, request, Response
from werkzeug.exceptions import BadRequest

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02394", methods=['GET', 'POST'])
def benchmark_test():
    response = Response(content_type="text/html;charset=UTF-8")
    
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    param = request.args.get("BenchmarkTest02394", "")
    bar = do_something(request, param)

    response = Response(bar, content_type="text/html;charset=UTF-8")
    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.set_data(response.get_data(as_text=True) % obj)
    return response

def do_something(request, param):
    from html import escape
    bar = escape(param)
    
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
