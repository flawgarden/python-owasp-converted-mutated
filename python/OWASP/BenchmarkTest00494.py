
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00494", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00494', '')
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value

        cmd = ""
        a1 = ""
        a2 = ""
        args = None
        os_name = os.name

        if os_name == 'nt':  # Windows
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = "echo"
            args = [a1, a2, cmd + " " + bar]
        else:  # Unix
            a1 = "sh"
            a2 = "-c"
            cmd = "ping -c1 "
            args = [a1, a2, cmd + bar]

        try:
            process = os.popen(' '.join(args))
            output = process.read()
            return render_template("output.html", output=output)
        except Exception as e:
            return render_template("error.html", error=str(e)), 500

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
