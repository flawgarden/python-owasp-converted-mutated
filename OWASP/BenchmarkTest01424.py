
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01424", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.values.keys()

    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01424":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(param)

    response = Response("Formatted like: {} and b.".format(bar))
    response.headers["X-XSS-Protection"] = "0"
    return response

class Test:

    def do_something(self, param):
        bar = param + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
