
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00543", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        if flag:
            values = request.values.getlist(name)
            if values:
                for value in values:
                    if value == "BenchmarkTest00543":
                        param = name
                        flag = False

    bar = ""
    if param:
        valuesList = ["safe", param, "moresafe"]
        valuesList.pop(0)  # remove the 1st safe value
        bar = valuesList[0]  # get the param value

    response = app.response_class(
        response=bar,
        status=200,
        mimetype='text/html'
    )
    response.headers['X-XSS-Protection'] = '0'
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
