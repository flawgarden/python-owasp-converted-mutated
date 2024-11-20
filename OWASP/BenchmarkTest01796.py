
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/cmdi-02/BenchmarkTest01796", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get("BenchmarkTest01796")
    bar = Test().do_something(param)

    cmd = Utils.get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = subprocess.Popen(args, env=dict(os.environ, **{'bar': bar}), cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return Utils.print_os_command_results(output, error)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:
    def do_something(self, param):
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

class Utils:
    @staticmethod
    def get_insecure_os_command_string():
        # Implement logic to return the insecure OS command string.
        return "/path/to/command"

    @staticmethod
    def print_os_command_results(output, error):
        return f"Output: {output.decode()} Error: {error.decode()}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
