
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01670", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        query_string = request.query_string.decode()
        paramval = "BenchmarkTest01670="
        param_loc = query_string.find(paramval)
        if param_loc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest01670' in query string."

        param = query_string[param_loc + len(paramval):]  # Assume it is the last param
        ampersand_loc = query_string.find("&", param_loc)
        if ampersand_loc != -1:
            param = query_string[param_loc + len(paramval):ampersand_loc]

        param = urllib.parse.unquote(param)

        bar = Test().do_something(param)

        return bar

class Test:

    def do_something(self, param):
        bar = param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')