
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02231", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = "text/html;charset=UTF-8"

    param = ""
    if request.args:
        param = request.args.get("BenchmarkTest02231", "")

    bar = do_something(param)

    response_headers = {"X-XSS-Protection": "0"}
    obj = [bar, "b"]
    return f"Formatted like: {obj[0]} and {obj[1]}.", response_headers

def do_something(param):
    a60610 = param
    b60610 = a60610 + " SafeStuff"
    b60610 = b60610[:-5] + "Chars"

    map60610 = {"key60610": b60610}
    c60610 = map60610["key60610"]
    d60610 = c60610[:-1]

    e60610 = base64.b64decode(base64.b64encode(d60610.encode())).decode()
    f60610 = e60610.split(" ")[0]

    g60610 = "barbarians_at_the_gate"
    bar = g60610  # Placeholder for the actual reflection logic

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
