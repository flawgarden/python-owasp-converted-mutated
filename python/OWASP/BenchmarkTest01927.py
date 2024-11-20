
import base64
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01927", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    param = request.headers.get("Referer", "")
    param = param # URL decoding would be handled automatically by Flask
    bar = do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = "0"
    return response

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
