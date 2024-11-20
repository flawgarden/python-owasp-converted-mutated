
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01596", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response(content_type="text/html;charset=UTF-8")
        values = request.values.getlist("BenchmarkTest01596")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        response.headers["X-XSS-Protection"] = "0"
        if bar is not None:
            response.set_data(bar)
        return response

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
