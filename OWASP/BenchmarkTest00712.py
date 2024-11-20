
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00712", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest00712")
    param = values[0] if values else ""

    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    response.headers['X-XSS-Protection'] = "0"
    obj = ["a", bar]
    response.data = "<!DOCTYPE html>\n<html>\n<body>\n<p>{}</p>\n</body>\n</html>".format(
        "Formatted like: {} and {}.".format(*obj))

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
