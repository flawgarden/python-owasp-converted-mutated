
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02581", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return process_request()
    return process_request()

def process_request():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02581="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02581' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = app.response_class()
    response.headers['X-XSS-Protection'] = '0'
    response.response = bar % ("a", "b")
    return response

def do_something(param):
    return escape_html(param)

def escape_html(param):
    return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
