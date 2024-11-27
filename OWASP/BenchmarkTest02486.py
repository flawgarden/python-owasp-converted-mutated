
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02486", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    values = request.args.getlist("BenchmarkTest02486")
    param = values[0] if values else ""

    bar = do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = "Formatted like: {} and {}.".format("a", bar)
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        sbxyz61588 = list(param)
        sbxyz61588[-1] = 'Z'
        bar = ''.join(sbxyz61588)
    return bar

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
