
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02124", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02124", "")  # or request.form.get(...) for POST
    bar = do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

def do_something(param):
    bar = param
    if param and len(param) > 1:
        bar = param[:-1] + 'Z'
    
    return bar

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
