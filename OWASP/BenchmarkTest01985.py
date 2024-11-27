
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01985", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name in common_headers:
            continue  # If standard header, move on to next one

        param = name  # Grabs the name of the first non-standard header as the parameter
        break

    bar = do_something(param)

    file_target = os.path.join(bar, "Test.txt")
    response_message = f"Access to file: '{file_target}' created."

    if os.path.exists(file_target):
        response_message += " And file already exists."
    else:
        response_message += " But file doesn't exist yet."

    return response_message

def do_something(param):
    bar = ""
    if param is not None:
        bar = param.encode('utf-8').decode('utf-8')
    return bar

common_headers = set(['Content-Type', 'User-Agent'])  # Add other common headers as needed

if __name__ == "__main__":
    app.run(host='0.0.0.0')
