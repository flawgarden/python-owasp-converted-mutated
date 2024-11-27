
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01493", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest01493", "")
    
    bar = Test().do_something(param)

    file_target = os.path.join(os.getenv('TESTFILES_DIR', 'testfiles'), bar)
    response += f"Access to file: '{file_target}' created.<br>"
    if os.path.exists(file_target):
        response += "And file already exists.<br>"
    else:
        response += "But file doesn't exist yet.<br>"
    
    return response

class Test:

    def do_something(self, param):
        bar = "safe!"
        map71009 = {}
        map71009["keyA-71009"] = "a_Value"
        map71009["keyB-71009"] = param
        map71009["keyC"] = "another_Value"
        bar = map71009.get("keyB-71009")
        bar = map71009.get("keyA-71009")
        
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
