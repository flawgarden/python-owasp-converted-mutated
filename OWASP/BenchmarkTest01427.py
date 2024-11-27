
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01427", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response("")
    param = ""
    flag = True
    names = request.args.to_dict().keys()

    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest01427":
                    param = name
                    flag = False

    bar = Test().do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = bar
    return response

class Test:

    def do_something(self, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
