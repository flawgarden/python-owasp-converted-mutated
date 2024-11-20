
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02407", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02407", "")
    bar = do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

def do_something(request, param):
    bar = param
    if param and len(param) > 1:
        sbxyz58438 = list(param)
        sbxyz58438[-1] = "Z"
        bar = ''.join(sbxyz58438)

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
