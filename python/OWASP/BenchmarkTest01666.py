
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01666", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01666="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return Response(f"getQueryString() couldn't find expected parameter 'BenchmarkTest01666' in query string.", status=400)

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:

    def do_something(self, param):
        bar = param
        if param is not None and len(param) > 1:
            sbxyz41549 = list(param)
            sbxyz41549[-1] = 'Z'
            bar = ''.join(sbxyz41549)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
