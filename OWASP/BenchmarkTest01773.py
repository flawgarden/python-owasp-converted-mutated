
import os
from flask import Flask, request, render_template
from werkzeug.utils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01773", methods=['GET', 'POST'])
def benchmark_test_01773():
    if request.method == 'GET':
        return benchmark_test_01773_post()
    return benchmark_test_01773_post()

def benchmark_test_01773_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.args.get("BenchmarkTest01773", "")
    bar = Test().do_something(param)
    response.headers['X-XSS-Protection'] = '0'
    length = 1
    if bar is not None:
        length = len(bar)
        response.data = bar.encode()[:length]
    return response

class Test:
    def do_something(self, param):
        bar = escape(param)
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
