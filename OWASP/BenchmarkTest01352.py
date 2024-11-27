
from flask import Flask, request, make_response
from werkzeug.utils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01352", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest01352", "")
    
    bar = Test().do_something(param)

    response = make_response(bar)
    response.headers["X-XSS-Protection"] = "0"
    return response

class Test:

    def do_something(self, param):
        bar = escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
