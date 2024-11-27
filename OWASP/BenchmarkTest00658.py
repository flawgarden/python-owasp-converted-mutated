
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00658", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    param = request.args.get("BenchmarkTest00658", "")
    bar = ""

    # Simple ? condition that assigns constant to bar on true condition
    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    cmd = ""
    os_name = os.name
    if os_name == "nt":
        cmd = "echo "

    try:
        process = os.popen(cmd + bar)
        response = process.read()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = str(e)

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
