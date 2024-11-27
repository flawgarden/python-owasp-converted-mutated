
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02199", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.args:
        param = request.args.get("BenchmarkTest02199", "")

    bar = do_something(request, param)

    file_target = os.path.abspath(bar)
    response.set_data(
        f"Access to file: '{file_target}' created.<br>"
    )
    if os.path.exists(file_target):
        response.set_data(response.get_data(as_text=True) + " And file already exists.<br>")
    else:
        response.set_data(response.get_data(as_text=True) + " But file doesn't exist yet.<br>")

    return response

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
