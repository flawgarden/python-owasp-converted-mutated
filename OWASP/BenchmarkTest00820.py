
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00820", methods=['GET', 'POST'])
def benchmark_test_00820():
    if request.method == 'GET':
        return benchmark_test_00820_post()

    return benchmark_test_00820_post()

def benchmark_test_00820_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00820="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00820' in query string.", 400

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = param
    if not bar:
        bar = "No cookie value supplied"

    response = make_response(f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: false")
    response.set_cookie("SomeCookie", bar, httponly=True, secure=False, path=request.path)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
