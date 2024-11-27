
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01441", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_content = ""
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01441":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = f"echo {bar}"
        args = [a1, a2, cmd]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = f"ping -c 1 {bar}"
        args = [a1, a2, cmd]

    try:
        process = os.popen(' '.join(args))
        response_content = process.read()
        return response_content
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

class Test:
    def do_something(self, request, param):
        # Assuming implementation for creating and using ThingInterface
        return param  # Placeholder logic, implement actual logic

if __name__ == "__main__":
    app.run(host='0.0.0.0')
