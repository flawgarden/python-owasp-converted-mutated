
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00571", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00571":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    cmd = "your_command_here"  # Replace with your insecure command string
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(" ".join(args) + " " + " ".join(args_env))
        response_data = process.read()
        return render_template("output.html", output=response_data)
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
