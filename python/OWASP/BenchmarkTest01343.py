
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01343", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response_type = "text/html;charset=UTF-8"
        param = request.form.get('BenchmarkTest01343', '')
        bar = Test().do_something(request, param)

        response_headers = {'X-XSS-Protection': '0'}
        return bar % ("a", "b"), response_type, response_headers

    return render_template("index.html")

class Test:

    def do_something(self, request, param):
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
