
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02334", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02334":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(request, param)

    arg_list = []
    os_name = os.name
    if os_name == 'nt':
        arg_list.append("cmd.exe")
        arg_list.append("/c")
    else:
        arg_list.append("sh")
        arg_list.append("-c")
    arg_list.append("echo " + bar)

    process = os.popen(' '.join(arg_list))
    output = process.read()
    process.close()

    return output

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
