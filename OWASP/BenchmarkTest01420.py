
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01420", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    flag = True
    for name in request.args:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01420":
                    param = name
                    flag = False

    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

class Test:

    @staticmethod
    def do_something(request, param):
        bar = param  # Here you would use an XSS protection encoder if needed
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
