
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-05/BenchmarkTest02580", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()


def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02580="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02580' in query string."

    param = query_string[param_loc + len(paramval):]  # Assume parameter is last
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = app.make_response(render_template("index.html", output=bar))
    response.headers["X-XSS-Protection"] = "0"
    
    return response


def do_something(param):
    sbxyz1658 = param + "_SafeStuff"
    return sbxyz1658


if __name__ == "__main__":
    app.run(host='0.0.0.0')
