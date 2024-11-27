
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02028", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get('BenchmarkTest02028')

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    file_target = os.path.join("path_to_testfiles", bar)
    response_message = f"Access to file: '{file_target}' created.<br>"

    if os.path.exists(file_target):
        response_message += " And file already exists."
    else:
        response_message += " But file doesn't exist yet."

    return response_message

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
