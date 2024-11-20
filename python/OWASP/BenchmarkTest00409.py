
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00409", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = {}
    param = request.args.get("BenchmarkTest00409", "")
    
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A' or switch_target == 'C' or switch_target == 'D':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    else:
        bar = "bobs_your_uncle"

    cmd = ""
    a1 = ""
    a2 = ""
    args = []

    os_name = os.name

    if os_name == 'nt':  # Windows
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:  # Unix-like
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))
        output = process.read()
        process.close()
        response['output'] = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response['error'] = str(e)

    return render_template("index.html", response=response)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
