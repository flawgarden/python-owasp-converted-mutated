
import os
from urllib.parse import quote
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01495", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest01495', '')  # Get parameter from the request
    bar = Test().do_something(param)

    start_uri_slashes = "//" if os.name != 'nt' else "/"

    try:
        file_uri = f"file:{start_uri_slashes}{quote(os.path.join('testfiles', bar.replace(' ', '_')))}"
        file_target = os.path.abspath(file_uri[5:])  # For 'file:', take the file path

        response_text = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            response_text += " And file already exists."
        else:
            response_text += " But file doesn't exist yet."

        return jsonify({'message': response_text})
    except Exception as e:
        return str(e), 500

class Test:
    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
