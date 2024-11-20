
from flask import Flask, request, Response
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02401", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    param = request.args.get("BenchmarkTest02401", "")
    bar = do_something(param)
    response.headers['X-XSS-Protection'] = '0'
    response.set_data(f"Formatted like: a and {bar}.")
    return response

def do_something(param):
    bar = html.escape(param)
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
