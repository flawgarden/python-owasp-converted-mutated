
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01525", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")
    param = request.args.get("BenchmarkTest01525", "")

    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data("Parameter value: " + bar)
    return response

class Test:

    def do_something(self, request, param):
        bar = param
        if param and len(param) > 1:
            sbxyz67457 = list(param)
            sbxyz67457[-1] = "Z"
            bar = ''.join(sbxyz67457)
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
