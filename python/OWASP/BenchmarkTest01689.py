
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01689", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01689="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01689' in query string."

    param = query_string[param_loc + len(paramval):] 
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = 'echo'

    args_env = {'Foo': 'bar'}
    
    try:
        process = os.popen(cmd + ' ' + bar)
        result = process.read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return f"Error: {str(e)}"

class Test:

    def do_something(self, param):
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
