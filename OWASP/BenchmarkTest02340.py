
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02340", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02340":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(request, param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = f"ls {bar}"
        args = [a1, a2, cmd]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        process.close()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]

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
