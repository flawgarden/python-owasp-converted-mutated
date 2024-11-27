
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02689", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest02689")

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", "b"]
    response.data = f"{bar % tuple(obj)}"
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
