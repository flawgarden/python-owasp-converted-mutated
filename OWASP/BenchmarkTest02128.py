
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02128", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02128', '')
    bar = do_something(param)

    response = app.make_response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1]
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
