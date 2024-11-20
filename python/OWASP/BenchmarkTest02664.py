
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-03/BenchmarkTest02664", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02664", "")
        bar = do_something(request, param)

        file_target = os.path.join(bar, "Test.txt")
        response_message = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            response_message += " And file already exists."
        else:
            response_message += " But file doesn't exist yet."
        return render_template("index.html", response=response_message)

    return render_template("index.html")

def do_something(request, param):
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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
