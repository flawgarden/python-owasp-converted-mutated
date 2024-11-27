
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02596", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Flask.response_class(content_type='text/html;charset=UTF-8')

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02596="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval}' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.response = bar
    return response

def do_something(param):
    bar = param  # Placeholder for ESAPI encoding for HTML
    # The actual ESAPI encoding for HTML should be implemented if needed.
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
