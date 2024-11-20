
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00822", methods=['GET', 'POST'])
def benchmark_test_00822():
    if request.method == 'GET':
        return benchmark_test_00822_post()

    return benchmark_test_00822_post()

def benchmark_test_00822_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00822" + "="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00822' in query string."

    param = query_string[param_loc + len(paramval):]  # Assume param is the last

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = None
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    response.headers['X-XSS-Protection'] = '0'
    response.data = f"Parameter value: {bar}".encode('utf-8')

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
