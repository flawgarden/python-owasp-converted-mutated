
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01661", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01661="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01661' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = Test().do_something(param)

    response = app.response_class()
    response.headers["X-XSS-Protection"] = "0"
    response.set_data("Formatted like: %s and %s." % ("a", bar))
    return response

class Test:
    def do_something(self, param):
        bar = urllib.parse.quote(param)  # HTML escaping can be replaced as needed
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
