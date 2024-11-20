
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02156", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02156', '')
    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error=str(e))

def do_something(param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

def get_insecure_os_command_string():
    return "echo"  # Example placeholder, modify according to actual command retrieval logic.

if __name__ == "__main__":
    app.run(host='0.0.0.0')
