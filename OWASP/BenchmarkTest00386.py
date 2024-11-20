
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00386", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest00386", "")

    bar = "safe!"
    map_8057 = {
        "keyA-8057": "a_Value",
        "keyB-8057": param,
        "keyC": "another_Value"
    }
    bar = map_8057.get("keyB-8057")
    bar = map_8057.get("keyA-8057")

    response.headers['X-XSS-Protection'] = "0"
    response.data = "Formatted like: {} and {}.".format(bar, "b")

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
