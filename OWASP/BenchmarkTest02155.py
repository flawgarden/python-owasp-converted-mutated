
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02155", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.form.get("BenchmarkTest02155", "")
    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        p.close()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error=str(e))

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def get_insecure_os_command_string():
    return "/some/insecure/command"  # Placeholder for the actual command

if __name__ == "__main__":
    app.run(host='0.0.0.0')
