
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01793", methods=['GET', 'POST'])
def benchmark_test_01793():
    if request.method == 'GET':
        return benchmark_test_01793_post()

    return benchmark_test_01793_post()

def benchmark_test_01793_post():
    param = request.form.get("BenchmarkTest01793")
    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        return output
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {e}"

class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[1]  # condition 'B', which is safe

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
    # Example of insecure command, replace with actual logic as needed
    return "echo"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
