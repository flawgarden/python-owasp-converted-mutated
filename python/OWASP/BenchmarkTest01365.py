
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01365", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01365', '')

        bar = Test().do_something(request, param)

        cmd = ''
        os_name = os.name
        if os_name == 'nt':
            cmd = 'echo '  # Equivalent command for Windows

        args_env = {"Foo": "bar"}

        try:
            process = subprocess.Popen(cmd + bar, env=args_env, shell=True, cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            return render_template("output.html", output=out.decode(), error=err.decode())
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return render_template("error.html", message=str(e))
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
