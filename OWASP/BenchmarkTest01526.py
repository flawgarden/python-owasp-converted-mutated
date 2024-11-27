
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01526", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_text = "text/html;charset=UTF-8"
    param = request.form.get("BenchmarkTest01526", "")

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "echo "

    try:
        p = os.popen(cmd + bar)
        output = p.read()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:
    def do_something(self, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
