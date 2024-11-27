
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00378", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = request.args.get("BenchmarkTest00378", "")
    sbxyz85125 = str(param)
    bar = sbxyz85125 + "_SafeStuff"

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.data = bar.format(*obj)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
