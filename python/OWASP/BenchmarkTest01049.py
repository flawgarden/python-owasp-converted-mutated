
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01049", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get('Referer', '')

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = f"Formatted like: a and {bar}."
    return response

class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)

            bar = values_list[0]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
