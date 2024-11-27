
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00803", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00803="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.set_data(
            f"getQueryString() couldn't find expected parameter 'BenchmarkTest00803' in query string."
        )
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = param

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
