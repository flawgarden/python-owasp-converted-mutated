
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02516", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    else:
        return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.args.getlist("BenchmarkTest02516")
    param = values[0] if values else ""

    bar = do_something(request, param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]
    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        output = process.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

def do_something(request, param):
    bar = "safe!"
    map74796 = {
        "keyA-74796": "a-Value",
        "keyB-74796": param,
        "keyC": "another-Value"
    }
    bar = map74796["keyB-74796"]
    return bar

def get_insecure_os_command_string():
    # Implement the method to return the insecure OS command string.
    return "echo"  # Example command

if __name__ == "__main__":
    app.run(host='0.0.0.0')
