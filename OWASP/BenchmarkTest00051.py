
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00051", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "text/html;charset=UTF-8"
    param = request.args.get("BenchmarkTest00051", "")

    a1, a2 = ("cmd.exe", "/c") if "Windows" in os.name else ("sh", "-c")
    command = f"echo {param}"
    args = [a1, a2, command]

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        p.close()
        return render_template("index.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - java.lang.ProcessBuilder(java.lang.String[]) Test Case")
        raise Exception(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
