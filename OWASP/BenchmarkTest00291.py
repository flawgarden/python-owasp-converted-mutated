
import urllib.parse
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00291", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    referer_header = request.headers.get("Referer")

    if referer_header:
        param = referer_header

    param = urllib.parse.unquote(param)

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    response = app.response_class()
    response.headers["X-XSS-Protection"] = "0"
    response.data = bar
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
