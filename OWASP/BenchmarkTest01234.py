
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__)
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles'  # Adjust the directory as needed

class Test:
    def do_something(self, param):
        # Simulated behavior of the ThingInterface
        return param

@app.route("/pathtraver-01/BenchmarkTest01234", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get('BenchmarkTest01234', '')
    bar = Test().do_something(param)

    file_target = os.path.join(TESTFILES_DIR, bar)
    response.data = f"Access to file: '{file_target}' created.<br>"

    if os.path.exists(file_target):
        response.data += " And file already exists."
    else:
        response.data += " But file doesn't exist yet."

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
