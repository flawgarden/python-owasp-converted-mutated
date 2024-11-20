
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01663", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01663="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter 'BenchmarkTest01663' in query string."

    param = query_string[param_loc + len(paramval):] 
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response = app.response_class()
    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.data = bar % tuple(obj)
    response.content_type = 'text/html;charset=UTF-8'
    
    return response

class Test:
    def do_something(self, param):
        bar = "safe!"
        map_36601 = {}
        map_36601["keyA-36601"] = "a_Value"
        map_36601["keyB-36601"] = param
        map_36601["keyC"] = "another_Value"
        bar = map_36601["keyB-36601"]
        bar = map_36601["keyA-36601"]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
