
import os
from flask import Flask, request, Response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00173", methods=['GET', 'POST'])
def benchmark_test_00173():
    if request.method == 'GET':
        return benchmark_test_00173_post()

    return benchmark_test_00173_post()

def benchmark_test_00173_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.headers.get("BenchmarkTest00173") is not None:
        param = request.headers.get("BenchmarkTest00173")

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map68097 = {
        "keyA-68097": "a-Value",
        "keyB-68097": param,
        "keyC": "another-Value"
    }
    bar = map68097["keyB-68097"]

    cmd = get_insecure_os_command_string()

    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        results = p.read()
        print_os_command_results(results, response)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = escape_html(str(e))
        return response

    return response

def get_insecure_os_command_string():
    # Replace with actual command retrieval logic as per your requirements
    return "your-command-here"

def print_os_command_results(results, response):
    response.data = results

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
