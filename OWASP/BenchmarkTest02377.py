
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02377", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02377", "")
    bar = do_something(param)

    file_target = os.path.join(bar, "Test.txt")
    response += "Access to file: '{}' created.".format(file_target)
    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."

    return response

def do_something(param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
