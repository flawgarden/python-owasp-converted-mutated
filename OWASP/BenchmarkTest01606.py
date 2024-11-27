
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01606", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        values = request.values.getlist("BenchmarkTest01606")
        param = values[0] if values else ""

        bar = Test().do_something(request, param)

        cmd = ""
        if "Windows" in os.name:
            cmd = get_os_command_string("echo")

        try:
            process = os.popen(cmd + bar)
            result = process.read()
            response.data = result
            response.mimetype = 'text/html;charset=UTF-8'
            return response
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            response.data = str(e).replace("<", "&lt;").replace(">", "&gt;")
            return response
    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

def get_os_command_string(command):
    return command

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
