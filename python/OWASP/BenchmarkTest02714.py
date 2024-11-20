
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-03/BenchmarkTest02714", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return execute_command()
    return execute_command()

def execute_command():
    response = app.response_class()
    param = request.values.get('BenchmarkTest02714')
    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]
    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        results = process.read()
        response.data = results
        response.content_type = "text/html;charset=UTF-8"
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return app.response_class(f"Error: {str(e)}", content_type="text/html;charset=UTF-8")

def do_something(param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def get_insecure_os_command_string():
    return "some_insecure_command"  # You need to define this according to your requirement

if __name__ == "__main__":
    app.run(host='0.0.0.0')
