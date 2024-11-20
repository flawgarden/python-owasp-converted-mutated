
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00895", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest00895")
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")

        bar = values_list[0] 

    arg_list = []

    os_name = os.name
    if os_name == 'nt':
        arg_list.append("cmd.exe")
        arg_list.append("/c")
    else:
        arg_list.append("sh")
        arg_list.append("-c")
    
    arg_list.append(f"echo {bar}")

    try:
        result = os.popen(' '.join(arg_list)).read()
        return result
    except Exception as e:
        print("Problem executing cmdi - python os.popen() Test Case")
        return str(e), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
