
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00176", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00176", "")
    param = param.encode().decode('utf-8')

    bar = param
    cmd = ""
    os_name = os.name
    
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}
    
    try:
        process = os.popen(cmd + bar)
        output = process.read()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
