
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def get_the_parameter(self, name):
        return self.request.args.get(name)

@app.route("/xss-01/BenchmarkTest00656", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    if request.method == 'POST':
        response = Response(content_type="text/html;charset=UTF-8")
        scr = SeparateClassRequest(request)
        param = scr.get_the_parameter("BenchmarkTest00656")
        if param is None:
            param = ""

        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param

        response.headers["X-XSS-Protection"] = "0"
        response.set_data("Parameter value: " + bar)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
