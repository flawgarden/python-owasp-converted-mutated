
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01288", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    
    return benchmark_test_post()

def benchmark_test_post():
    param = request.form.get("BenchmarkTest01288", "")
    bar = Test().do_something(param)

    cmd = "your_command_here"  # Replace with the function to get the insecure command string
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(f"{cmd} {bar}")  # You can adapt this to fit your needs
        output = p.read()
        return render_template("index.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("index.html", error=str(e))

class Test:
    def do_something(self, param):
        bar = "safe!"
        map58555 = {
            "keyA-58555": "a-Value",
            "keyB-58555": param,
            "keyC": "another-Value"
        }
        bar = map58555.get("keyB-58555")
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
