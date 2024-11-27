
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name)

@app.route("/xss-01/BenchmarkTest00882", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00882")

    bar = None
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    response.headers['X-XSS-Protection'] = '0'
    response.set_data(bar)
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
