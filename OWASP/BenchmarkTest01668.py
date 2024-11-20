
from flask import Flask, request

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01668", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01668="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param.replace('+', ' ')  # URL decode process
    bar = Test().do_something(param)

    return bar

class Test:

    def do_something(self, param):
        bar = "safe!"
        map56839 = {
            "keyA-56839": "a_Value",
            "keyB-56839": param,
            "keyC": "another_Value"
        }
        bar = map56839["keyB-56839"]
        bar = map56839["keyA-56839"]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
