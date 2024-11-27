
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02512", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest02512")
    param = values[0] if values else ""

    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        response = print_os_command_results(p)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = escape_html(str(e))
    return response

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def get_insecure_os_command_string():
    # Implementation to get the command string
    return "insecure_command"

def print_os_command_results(process):
    return process.read()

def escape_html(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
