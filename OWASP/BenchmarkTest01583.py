
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01583", methods=['GET', 'POST'])
def benchmark_test():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.args.getlist("BenchmarkTest01583")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = f"<!DOCTYPE html>\n<html>\n<body>\n<p>Formatted like: a and {bar}.\n</p>\n</body>\n</html>"
    return response

class Test:

    def do_something(self, request, param):
        sbxyz82559 = str(param)
        bar = sbxyz82559 + "_SafeStuff"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
