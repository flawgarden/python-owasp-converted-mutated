
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest02056", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = make_response()
        param = ""

        if 'Referer' in request.headers:
            param = request.headers['Referer']

        param = urllib.parse.unquote(param)

        bar = do_something(param)

        response.headers['X-XSS-Protection'] = "0"
        response.set_data(bar)
        return response

def do_something(param):
    bar = "safe!"
    map88820 = {}
    map88820["keyA-88820"] = "a-Value"
    map88820["keyB-88820"] = param
    map88820["keyC"] = "another-Value"
    bar = map88820["keyB-88820"]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
