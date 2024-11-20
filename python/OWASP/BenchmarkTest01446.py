
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def decode_param(param):
    if param is not None:
        return param.encode('utf-8').decode('base64')
    return ""

@app.route("/cmdi-01/BenchmarkTest01446", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = ""
        flag = True
        for name in request.args:
            values = request.args.getlist(name)
            if values:
                for value in values:
                    if value == 'BenchmarkTest01446':
                        param = name
                        flag = False
                        break

        bar = decode_param(param)

        cmd = ""
        if os.name == 'nt':
            cmd = "echo"

        args_env = {"Foo": "bar"}
        try:
            process = os.popen(f'{cmd} {bar}', 'r')
            results = process.read()
            return render_template("result.html", results=results)
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return render_template("error.html", message=str(e))
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')
