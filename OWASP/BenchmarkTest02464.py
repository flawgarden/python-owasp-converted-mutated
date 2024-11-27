
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02464", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    if request.method == 'POST':
        response = "Access to file: '"
        values = request.values.getlist("BenchmarkTest02464")
        param = values[0] if values else ""

        bar = do_something(request, param)

        file_target = os.path.abspath(bar)
        response += file_target + "' created."

        if os.path.exists(file_target):
            response += " And file already exists."
        else:
            response += " But file doesn't exist yet."

        return response

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
