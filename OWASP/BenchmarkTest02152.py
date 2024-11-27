
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02152", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content_type = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest02152", "")
    bar = do_something(param)

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
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        p = os.popen(' '.join(args))
        result = p.read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    if param:
        bar = param.encode('utf-8').encode('base64').decode('utf-8').strip()
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
