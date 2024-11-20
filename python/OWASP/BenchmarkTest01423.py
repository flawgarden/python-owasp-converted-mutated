
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01423", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01423":
                    param = name
                    flag = False
                    break

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    obj = [bar, "b"]
    response.set_data("Formatted like: %s and %s." % (obj[0], obj[1]))
    
    return response

class Test:

    def do_something(self, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
