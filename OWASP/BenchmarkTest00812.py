
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00812", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00812="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter 'BenchmarkTest00812' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = "This_should_always_happen" if (7 * 18) + 106 > 200 else param

    response.headers['X-XSS-Protection'] = "0"
    response.data = bar
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
