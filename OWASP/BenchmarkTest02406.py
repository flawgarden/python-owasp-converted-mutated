
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02406", methods=['GET', 'POST'])
def benchmark_test_02406():
    if request.method == 'GET':
        return benchmark_test_02406_post()
    return benchmark_test_02406_post()

def benchmark_test_02406_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.args.get('BenchmarkTest02406', '')
    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

def do_something(param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
