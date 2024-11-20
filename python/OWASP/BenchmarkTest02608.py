
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02608", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_text = "text/html;charset=UTF-8"
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02608="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02608' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    bar = do_something(param)
    
    response = app.response_class(response=f"Parameter value: {bar}", content_type=response_text)
    response.headers["X-XSS-Protection"] = "0"
    return response

def do_something(param):
    bar = param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
