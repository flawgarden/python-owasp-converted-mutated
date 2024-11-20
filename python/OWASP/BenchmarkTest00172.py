
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00172", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Flask.response_class(content_type='text/html;charset=UTF-8')

    param = request.headers.get("BenchmarkTest00172", "")
    param = urllib.parse.unquote(param)

    bar = "safe!"
    map59408 = {}
    map59408["keyA-59408"] = "a-Value"
    map59408["keyB-59408"] = param
    map59408["keyC"] = "another-Value"
    bar = map59408["keyB-59408"]

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

    return response

def get_insecure_os_command_string():
    return "your_command_here"  # Example placeholder for actual command

if __name__ == "__main__":
    app.run(host='0.0.0.0')
