
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01770", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['X-XSS-Protection'] = '0'
    param = request.args.get("BenchmarkTest01770", "")
    bar = Test().do_something(param)
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    response.mimetype = 'text/html;charset=UTF-8'
    
    return response

class Test:

    def do_something(self, param):
        sbxyz41282 = str(param)
        bar = sbxyz41282 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
