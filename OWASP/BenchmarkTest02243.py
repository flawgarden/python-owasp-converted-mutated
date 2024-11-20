
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02243", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02243', '')

        bar = do_something(param)

        arg_list = []
        os_name = os.name
        if os_name == 'nt':
            arg_list.append("cmd.exe")
            arg_list.append("/c")
        else:
            arg_list.append("sh")
            arg_list.append("-c")

        arg_list.append("echo " + bar)

        try:
            result = subprocess.run(arg_list, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            print("Problem executing cmdi - subprocess Test Case")
            return str(e)

    return render_template("index.html")

def do_something(param):
    bar = "safe!"
    map_19941 = {}
    map_19941["keyA-19941"] = "a-Value"
    map_19941["keyB-19941"] = param
    map_19941["keyC"] = "another-Value"
    bar = map_19941["keyB-19941"]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
