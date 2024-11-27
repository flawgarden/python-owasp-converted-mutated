
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00862", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = request.args.get('BenchmarkTest00862')

    bar = ""

    num = 106

    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    file_target = os.path.join('path/to/test/files/directory', bar)
    response = f"Access to file: '{file_target}' created."

    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
