
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00801", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return make_response("Unsupported method", 405)

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00801="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00801' in query string.", 400

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = param

    response = make_response()
    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
