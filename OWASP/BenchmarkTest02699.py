
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-03/BenchmarkTest02699", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.values.get("BenchmarkTest02699")
    bar = do_something(param)

    a1, a2 = ("cmd.exe", "/c") if "Windows" in os.name else ("sh", "-c")
    args = [a1, a2, f"echo {bar}"]

    process = os.popen(' '.join(args))
    result = process.read()
    process.close()
    
    return result

def do_something(param):
    num = 106
    return "This should never happen" if (7 * 42) - num > 200 else param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
