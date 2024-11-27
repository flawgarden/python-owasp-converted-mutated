
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00731", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest00731")
    param = values[0] if values else ""

    bar = param

    arg_list = []

    os_name = os.name
    if os_name == 'nt':  # Windows
        arg_list.extend(["cmd.exe", "/c"])
    else:
        arg_list.extend(["sh", "-c"])
    arg_list.append(f"echo {bar}")

    try:
        process = os.popen(" ".join(arg_list))
        response = process.read()
        process.close()
    except Exception as e:
        print("Problem executing command - Python subprocess Test Case")
        return str(e)

    return render_template("index.html", output=response)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
