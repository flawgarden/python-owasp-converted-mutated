
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02327", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = ""
        flag = True
        names = request.args.keys() if request.method == 'GET' else request.form.keys()

        for name in names:
            values = request.form.getlist(name)
            if values:
                for value in values:
                    if value == "BenchmarkTest02327":
                        param = name
                        flag = False
                        break

        bar = do_something(param)

        response.headers['X-XSS-Protection'] = '0'
        length = 1
        if bar is not None:
            length = len(bar)
            response.data = bar

        return response

def do_something(param):
    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        del values_list[0]  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
