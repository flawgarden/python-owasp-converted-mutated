
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01584", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'
        
        values = request.values.getlist("BenchmarkTest01584")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        response.headers['X-XSS-Protection'] = '0'
        response.set_data(bar % ("a", "b"))
        return response

class Test:
    def do_something(self, request, param):
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
