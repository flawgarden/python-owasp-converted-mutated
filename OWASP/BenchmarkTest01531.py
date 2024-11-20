
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01531", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01531", "")
    bar = Test().do_something(param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = subprocess.Popen(args, env={"BAR": bar}, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return print_os_command_results(output, error)
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {str(e)}"

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

def get_insecure_os_command_string():
    # Replace this with the logic to get the insecure OS command string
    return "example_command"

def print_os_command_results(output, error):
    return f"Output: {output.decode('utf-8')}<br>Error: {error.decode('utf-8')}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
