
from flask import Flask, request
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-05/BenchmarkTest02582", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_get(request)


def do_get(request):
    return do_post(request)


def do_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02582="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02582' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    return bar


def do_something(request, param):
    sbxyz18070 = str(param)
    bar = sbxyz18070 + "_SafeStuff"

    return bar


@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404


if __name__ == "__main__":
    app.run(host='0.0.0.0')
