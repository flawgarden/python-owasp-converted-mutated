
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01795", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = {"Content-Type": "text/html;charset=UTF-8"}

    param = request.values.get("BenchmarkTest01795")

    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return escape_html(str(e))

class Test:

    def do_something(self, request, param):
        bar = ""
        if param is not None:
            values_list = []
            values_list.append("safe")
            values_list.append(param)
            values_list.append("moresafe")

            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[0]  # get the param value

        return bar

def get_insecure_os_command_string():
    # Implement your logic to retrieve an insecure command string
    return "your_command_here"

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
