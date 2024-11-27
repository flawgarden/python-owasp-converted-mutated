
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            values_list = ['safe', param, 'moresafe']
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

@app.route("/cmdi-01/BenchmarkTest01286", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01286', '')
        bar = Test().do_something(param)

        cmd = ""
        a1 = ""
        a2 = ""
        args = []
        os_name = os.name

        if os_name == 'nt':
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = f"echo"
            args = [a1, a2, cmd + " " + bar]
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = "ping -c 1 "
            args = [a1, a2, cmd + bar]

        try:
            process = os.popen(" ".join(args))
            output = process.read()
            return render_template("result.html", output=output)
        except Exception as e:
            return f"Problem executing cmdi - TestCase: {e}"

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
