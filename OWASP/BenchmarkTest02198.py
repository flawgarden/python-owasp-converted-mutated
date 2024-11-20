
from flask import Flask, request, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02198", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        return handle_post(request)

def handle_post(request):
    response = ""
    response += "Content Type: text/html;charset=UTF-8\n"

    param = ""
    map = request.form.to_dict()

    if map:
        values = map.get("BenchmarkTest02198")
        if values:
            param = values

    bar = do_something(request, param)

    file_target = os.path.join("your_test_files_directory", bar)
    response += "Access to file: '{}' created.".format(file_target)

    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."

    return response

def do_something(request, param):
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
