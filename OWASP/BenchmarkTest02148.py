
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02148", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get('BenchmarkTest02148', '')
    bar = do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""

    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))
        response = process.read()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response += str(e)

    return render_template("result.html", output=response)

def do_something(param):
    a17988 = param
    b17988 = a17988 + " SafeStuff"
    b17988 = b17988[:-5] + "Chars"  # replace "Chars"
    map17988 = {"key17988": b17988}
    c17988 = map17988["key17988"]
    d17988 = c17988[:-1]
    e17988 = d17988.encode('utf-8').decode('utf-8')  # dummy encoding/decoding
    f17988 = e17988.split(" ")[0]

    # Mocking ThingInterface and ThingFactory
    bar = "safe_output"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
