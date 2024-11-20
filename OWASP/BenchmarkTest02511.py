
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02511", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    content_type = "text/html;charset=UTF-8"
    response.headers['Content-Type'] = content_type

    values = request.values.getlist("BenchmarkTest02511")
    param = values[0] if values else ""

    bar = do_something(request, param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(" ".join(args) + " " + " ".join(args_env))
        output = process.read()
        response.set_data(output)
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(encode_for_html(str(e)))
        return response

def do_something(request, param):
    num = 196
    if (500 / 42) + num > 200:
        return param
    return "This should never happen"

def get_insecure_os_command_string():
    # Placeholder for actual implementation; should be replaced with proper logic
    return '/path/to/command'

def encode_for_html(data):
    return data.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
