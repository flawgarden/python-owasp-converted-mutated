
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01259", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest01259", "")
    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = "Formatted like: {} and {}.".format(bar, "b")
    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-26093": "a-Value",
            "keyB-26093": param,
            "keyC": "another-Value"
        }
        bar = map_.get("keyB-26093")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
