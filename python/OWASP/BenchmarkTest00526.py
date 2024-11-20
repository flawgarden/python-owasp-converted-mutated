
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00526", methods=['GET', 'POST'])
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
                if value == "BenchmarkTest00526":
                    param = name
                    flag = False
                    break

    bar = param
    file_target = os.path.join(bar, "Test.txt")

    response_message = "Access to file: '{}' created.".format(file_target)
    if os.path.exists(file_target):
        response_message += " And file already exists."
    else:
        response_message += " But file doesn't exist yet."

    return response_message

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
