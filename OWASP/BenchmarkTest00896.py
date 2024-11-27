
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest00896", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = request.form.get('BenchmarkTest00896')
    
    if (7 * 42) - 86 > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    arg_list = []

    if os.name == 'nt':
        arg_list.append("cmd.exe")
        arg_list.append("/c")
    else:
        arg_list.append("sh")
        arg_list.append("-c")
    
    arg_list.append(f"echo {bar}")

    process = os.popen(' '.join(arg_list))
    results = process.read()
    
    return render_template("index.html", results=results)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
