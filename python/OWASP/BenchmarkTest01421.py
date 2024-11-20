
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01421", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response(content_type="text/html;charset=UTF-8")

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01421":
                    param = name
                    flag = False

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    obj = ("a", bar)
    response.set_data("Formatted like: %s and %s." % obj)
    return response

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
