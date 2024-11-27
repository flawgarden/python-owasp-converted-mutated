
import urllib.parse
from flask import Flask, request

app = Flask(__name__)

@app.route("/xss-05/BenchmarkTest02591", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_data = "text/html;charset=UTF-8"
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02591="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02591' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = f'Content-Type: {response_data}\n'
    response += 'X-XSS-Protection: 0\n'
    response += f'Formatted like: {bar} and b.'

    return response

def do_something(param):
    sbxyz9811 = str(param)
    bar = sbxyz9811 + "_SafeStuff"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
