
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00910", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return render_template("index.html")

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00910", "")

    bar = ""
    num = 106

    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    cmd = ""
    osName = os.name
    if osName == 'nt':
        cmd = "echo"

    argsEnv = {"Foo": "bar"}
    
    try:
        p = os.popen(cmd + " " + bar)
        output = p.read()
        return render_template("index.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("index.html", error=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
