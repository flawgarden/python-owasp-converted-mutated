
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-03/BenchmarkTest02518", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.form.getlist("BenchmarkTest02518")
    param = values[0] if values else ""

    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {bar}")  # Simplified command execution
        output = p.read()
        p.close()
        return response

    except Exception as e:
        print("Problem executing cmd - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # Condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def get_insecure_os_command_string():
    # Replace with your actual implementation of command fetching
    return "your_command_here"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
