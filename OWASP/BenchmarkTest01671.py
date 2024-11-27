
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01671", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    param_val = "BenchmarkTest01671="
    param_loc = query_string.find(param_val)

    if param_loc == -1:
        response.set_data("getQueryString() couldn't find expected parameter 'BenchmarkTest01671' in query string.")
        return response

    param = query_string[param_loc + len(param_val):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(param_val):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

class Test:

    @staticmethod
    def do_something(param):
        bar = escape_html(param)
        return bar

def escape_html(raw):
    return urllib.parse.quote_plus(raw)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
