
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00657", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00657", "")
    bar = "safe!"
    map27260 = {
        "keyA-27260": "a_Value",
        "keyB-27260": param,
        "keyC": "another_Value"
    }
    bar = map27260["keyB-27260"]
    bar = map27260["keyA-27260"]

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Windows specific command

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error_message=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
