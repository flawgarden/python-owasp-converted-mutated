
import urllib.parse
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00145", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("Referer") is not None:
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map17589 = {
        "keyA-17589": "a-Value",
        "keyB-17589": param,
        "keyC": "another-Value"
    }
    bar = map17589.get("keyB-17589")

    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", "b"]
    response.set_data(response.response_class.format("{}".format(bar), obj, locale='en_US'))
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
