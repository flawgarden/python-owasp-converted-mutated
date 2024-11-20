
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01593", methods=['GET', 'POST'])
def benchmark_test_01593():
    if request.method == 'GET':
        return benchmark_test_01593_post()

    if request.method == 'POST':
        return benchmark_test_01593_post()

def benchmark_test_01593_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.values.getlist("BenchmarkTest01593")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

class Test:

    def do_something(self, request, param):
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
