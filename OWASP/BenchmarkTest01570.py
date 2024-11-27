
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01570", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = []
    response.append("Content-Type: text/html;charset=UTF-8")

    values = request.values.getlist("BenchmarkTest01570")
    param = values[0] if values else ""

    bar = Test().do_something(request, param)

    file_target = os.path.join("path/to/test/files", bar)
    response.append(f"Access to file: '{file_target}' created.")

    if os.path.exists(file_target):
        response.append(" And file already exists.")
    else:
        response.append(" But file doesn't exist yet.")

    return '<br>'.join(response)

class Test:

    def do_something(self, request, param):
        bar = ""
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
