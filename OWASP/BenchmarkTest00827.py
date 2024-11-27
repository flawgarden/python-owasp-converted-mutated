
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00827", methods=['GET', 'POST'])
def benchmark_test_00827():
    if request.method == 'GET':
        return benchmark_test_00827_post()

    return benchmark_test_00827_post()

def benchmark_test_00827_post():
    response = Flask.response_class(content_type="text/html;charset=UTF-8")
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00827="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response.data = f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")
        bar = values_list[1]

    cmd = "your_insecure_command_here"  # replace with actual command retrieval method
    args_env = [bar]

    try:
        process = os.popen(cmd + ' ' + ' '.join(args_env))
        output = process.read()
        response.data = output
        return response
    except Exception as e:
        response.data = str(e)
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
