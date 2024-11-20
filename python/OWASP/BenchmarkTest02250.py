
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02250", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02250', '')

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # For Windows
        cmd = "echo "

    try:
        process = subprocess.Popen(cmd + bar, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return "<pre>" + output.decode() + "</pre>"
    except Exception as e:
        return "<pre>" + str(e) + "</pre>"

def do_something(param):
    bar = "safe!"
    map94176 = {
        "keyA-94176": "a-Value",
        "keyB-94176": param,
        "keyC": "another-Value"
    }
    bar = map94176["keyB-94176"]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
