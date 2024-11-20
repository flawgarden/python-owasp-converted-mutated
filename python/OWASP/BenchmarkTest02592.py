
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02592", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02592="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        response.set_data(
            f"getQueryString() couldn't find expected parameter '{'BenchmarkTest02592'}' in query string."
        )
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = (bar, 'b')
    response.set_data(f"Formatted like: {obj[0]} and {obj[1]}.")
    return response

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        sbxyz52014 = list(param)
        sbxyz52014[-1] = 'Z'
        bar = ''.join(sbxyz52014)

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
