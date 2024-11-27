
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00908", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest00908")

    bar = None
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

    cmd = "your_insecure_command_here"
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        return response_content_type, output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
