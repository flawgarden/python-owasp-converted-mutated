
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01239", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = {}
    param = request.args.get("BenchmarkTest01239", "")
    
    bar = Test().do_something(param)
    file_name = os.path.join('testfiles/', bar)

    try:
        with open(file_name, 'w') as fos:
            response['message'] = "Now ready to write to file: " + file_name
    except Exception as e:
        print("Couldn't open FileOutputStream on file: '" + file_name + "'")
    
    return render_template("index.html", response=response)

class Test:

    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
