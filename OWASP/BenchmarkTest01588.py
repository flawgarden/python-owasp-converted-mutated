
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01588", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest01588")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = "0"
    response.data = bar % ("a", "b")
    return response

class Test:

    def do_something(self, request, param):
        num = 86
        if (7 * 42) - num > 200:
            return "This_should_always_happen"
        else:
            return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
