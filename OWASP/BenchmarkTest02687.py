
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02687", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_get(request)

def do_get(request):
    return do_post(request)

def do_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02687", "")
    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.data = bar % tuple(obj)

    return response

def do_something(request, param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
