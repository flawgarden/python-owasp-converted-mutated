
import os
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01792", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = request.args.get("BenchmarkTest01792", "")

    bar = Test().do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd, bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(html_escape(str(e)))

    return response

class Test:

    def do_something(self, param):
        bar = param
        return bar

def html_escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
