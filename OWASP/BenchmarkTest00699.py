
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00699", methods=['GET', 'POST'])
def benchmark_test_00699():
    if request.method == 'GET':
        return benchmark_test_00699_post()

    return benchmark_test_00699_post()

def benchmark_test_00699_post():
    values = request.args.getlist("BenchmarkTest00699")
    param = values[0] if values else ""

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

    file_target = os.path.join(bar, "Test.txt")
    response = f"Access to file: '{file_target}' created."

    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
