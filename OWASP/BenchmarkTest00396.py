
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00396", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest00396', '')
        bar = ""

        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        a1, a2 = ("cmd.exe", "/c") if "Windows" in os.name else ("sh", "-c")
        args = [a1, a2, "echo " + bar]

        pb = os.popen(" ".join(args))
        output = pb.read()
        pb.close()
        
        return output

    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
