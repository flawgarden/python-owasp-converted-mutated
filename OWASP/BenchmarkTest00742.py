
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00742", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.args.getlist("BenchmarkTest00742")
    param = values[0] if values else ""

    bar = "safe!"
    map62435 = {
        "keyA-62435": "a_Value",
        "keyB-62435": param,
        "keyC": "another_Value"
    }
    bar = map62435["keyB-62435"]
    bar = map62435["keyA-62435"]

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e))
        return response

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
