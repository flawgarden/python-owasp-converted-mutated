
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01791", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.form.get("BenchmarkTest01791")
    bar = Test().do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Windows command

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        response.data = output.encode('utf-8')
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e).encode('utf-8')
        return response

    return response

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
