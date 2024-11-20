
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02303", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02303":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    file_name = None
    try:
        file_name = os.path.join('path_to_test_files', bar)  # Replace with actual directory
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_data = f"The beginning of file: '{file_name}' is:\n\n" + b.decode('utf-8', errors='ignore')
            return response_data
    except Exception as e:
        return f"Problem getting FileInputStream: {str(e)}"

def do_something(param):
    bar = None
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
