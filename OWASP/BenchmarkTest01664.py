
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01664", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return Response("Method not allowed", status=405)

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    param_val = "BenchmarkTest01664="
    param_loc = query_string.find(param_val)
    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter 'BenchmarkTest01664' in query string.", 400

    param = query_string[param_loc + len(param_val):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(param_val):ampersand_loc]
    
    param = urllib.parse.unquote(param)
    
    bar = Test().do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:

    def do_something(self, param):
        bar = param  # In a real scenario, use an appropriate HTML escaping method
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
