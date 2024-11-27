
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02146", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02146", "")
        bar = do_something(request, param)

        cmd = ""
        os_name = os.name
        if os_name == 'nt':  # Windows
            cmd = "echo "

        try:
            process = os.popen(cmd + bar)
            output = process.read()
            return render_template("output.html", output=output)
        except Exception as e:
            return render_template("error.html", error=str(e))

    return render_template("index.html")

def do_something(request, param):
    bar = ""
    if param:
        values_list = []
        values_list.append("safe")
        values_list.append(param)
        values_list.append("moresafe")

        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
