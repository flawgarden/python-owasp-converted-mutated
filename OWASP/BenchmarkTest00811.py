
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00811", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00811="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter '{paramval.rstrip('=')}' in query string."
        return response

    param = query_string[param_loc + len(paramval):]  # Assume parameter is last
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    response.headers['X-XSS-Protection'] = "0"
    response.data = ''.join(bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
