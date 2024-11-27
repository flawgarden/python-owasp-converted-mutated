
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02381", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.args.get('BenchmarkTest02381', "")
        bar = do_something(request, param)

        file_name = os.path.join("testfiles", bar)

        try:
            with open(file_name, 'w') as fos:
                response.data = f"Now ready to write to file: {file_name}"
        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    
        return response

def do_something(request, param):
    bar = "safe!"
    map75774 = {
        "keyA-75774": "a_Value",
        "keyB-75774": param,
        "keyC": "another_Value"
    }
    bar = map75774["keyB-75774"]
    bar = map75774["keyA-75774"]
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
