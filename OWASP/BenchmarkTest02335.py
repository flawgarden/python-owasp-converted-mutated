
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02335", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    for name in request.form.keys():
        values = request.form.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02335":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    a1 = "cmd.exe" if os.name == 'nt' else "sh"
    a2 = "/c" if os.name == 'nt' else "-c"
    args = [a1, a2, "echo " + bar]

    try:
        process = os.popen(' '.join(args))
        result = process.read()
        return result
    except Exception as e:
        print("Problem executing command - ProcessBuilder Test Case")
        return str(e)

def do_something(param):
    bar = "alsosafe"
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
