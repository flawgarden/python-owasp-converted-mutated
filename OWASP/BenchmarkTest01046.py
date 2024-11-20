
from flask import Flask, request, make_response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest01046", methods=['GET', 'POST'])
def benchmark_test_01046():
    if request.method == 'GET':
        return benchmark_test_01046_post()
    return benchmark_test_01046_post()

def benchmark_test_01046_post():
    response = make_response()

    param = request.headers.get("Referer", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", bar]
    response.set_data("<!DOCTYPE html>\n<html>\n<body>\n<p>{}</p>\n</body>\n</html>".format(
        "Formatted like: {} and {}.".format(obj[0], obj[1])))
    response.mimetype = "text/html;charset=UTF-8"
    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-95803": "a-Value",
            "keyB-95803": param,
            "keyC": "another-Value"
        }
        bar = map_["keyB-95803"]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
