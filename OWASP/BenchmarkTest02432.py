
from flask import Flask, request, render_template
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02432", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get("BenchmarkTest02432", default="", type=str)

        bar = do_something(request, param)

        cmd = ""
        a1 = ""
        a2 = ""
        args = []
        os_name = subprocess.run(['uname'], stdout=subprocess.PIPE).stdout.decode().strip()

        if "Windows" in os_name:
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = "echo "
            args = [a1, a2, cmd + bar]
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = "ls "
            args = [a1, a2, cmd + bar]

        args_env = {"foo": "bar"}

        try:
            result = subprocess.run(args, env=args_env, cwd=".", check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode()
            return output
        except subprocess.CalledProcessError as e:
            return render_template("error.html", error_message=str(e))

def do_something(request, param):
    bar = "safe!"
    map15850 = {
        "keyA-15850": "a-Value",
        "keyB-15850": param,
        "keyC": "another-Value"
    }
    bar = map15850.get("keyB-15850")
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
