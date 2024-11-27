
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02230", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest02230', '')

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.data = f"Formatted like: {obj[0]} and {obj[1]}."

    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        sbxyz51189 = list(param)
        sbxyz51189[-1] = 'Z'
        bar = ''.join(sbxyz51189)

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
