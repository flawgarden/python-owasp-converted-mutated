
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest02724", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest02724", "")
    bar = do_something(param)

    # Simulate session storage
    request.session[bar] = "10340"

    return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

def do_something(param):
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        return param
    elif switch_target == 'B':
        return "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        return param
    else:
        return "bobs_your_uncle"

def encode_for_html(text):
    return text  # Placeholder for HTML encoding logic

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
