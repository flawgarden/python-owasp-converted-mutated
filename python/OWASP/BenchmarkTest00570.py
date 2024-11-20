
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00570", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    param = ""
    flag = True
    names = request.args.keys()
    
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00570":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.remove("safe")  # remove the 1st safe value
        bar = values_list[1]  # get the last 'safe' value

    cmd = "your_command_here" # replace with function to get the insecure OS command string
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args), 'r', bar)  # using os.popen for simplicity
        response = process.read()
    except Exception as e:
        response = str(e)

    return render_template("index.html", output=response)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
