
import os
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00048", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    elif request.method == 'POST':
        return benchmark_test_post(request)

def benchmark_test_post(request):
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00048="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00048' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    response.headers['X-XSS-Protection'] = '0'
    response.data = str(param).encode()

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
