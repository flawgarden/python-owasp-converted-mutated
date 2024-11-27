
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01509", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = request.values.get("BenchmarkTest01509", "")
    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    
    return response

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')