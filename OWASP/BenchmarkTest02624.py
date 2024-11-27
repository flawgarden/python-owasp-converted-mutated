
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02624", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02624="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02624' in query string."

    param = query_string[param_loc + len(paramval):]

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    # Set session attribute
    request.environ['beaker.session']['userid'] = bar

    return f"Item: 'userid' with value: '{bar}' saved in session."

def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-3141": "a-Value",
        "keyB-3141": param,
        "keyC": "another-Value"
    }
    bar = map_.get("keyB-3141")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
