
from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-01/BenchmarkTest01440", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        content_type='text/html;charset=UTF-8'
    )

    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest01440":
                    param = name
                    flag = False

    bar = Test().do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # For Windows

    try:
        result = subprocess.run(cmd + bar, shell=True, capture_output=True, text=True)
        response.data = result.stdout
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)

    return response


class Test:

    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
