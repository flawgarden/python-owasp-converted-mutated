
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00808", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00808="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        response.set_data("getQueryString() couldn't find expected parameter 'BenchmarkTest00808' in query string.")
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)

        bar = values_list[1]

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", "b"]
    response.set_data(bar % obj)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
