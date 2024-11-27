
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01906", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01906", "")
    param = param.encode('utf-8').decode('utf-8')

    bar = do_something(param)

    file_name = None
    fos = None

    try:
        file_name = os.path.join('testfiles', bar)

        with open(file_name, 'w') as fos:
            return f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    
    return "Error occurred"

def do_something(param):
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
