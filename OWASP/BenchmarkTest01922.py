
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01922", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    if request.headers.get("Referer") is not None:
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.set_data(bar % tuple(obj))

    return response

def do_something(request, param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
