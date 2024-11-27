
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01364", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = ""
    if request.args:
        param = request.args.get("BenchmarkTest01364", "")

    bar = Test().do_something(param)

    cmd = Utils.get_insecure_os_command_string()

    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        result = p.read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return Utils.encode_for_html(str(e))

class Test:
    def do_something(self, param):
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

class Utils:
    @staticmethod
    def get_insecure_os_command_string():
        # Implement your logic to return the command string
        return "your_command_here"

    @staticmethod
    def encode_for_html(message):
        return message.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
