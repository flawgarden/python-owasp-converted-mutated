
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02489", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.form.getlist("BenchmarkTest02489")
    param = values[0] if values else ""

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    
    return response

def do_something(param):
    bar = param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
