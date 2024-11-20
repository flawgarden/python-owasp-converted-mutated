
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, key):
        return self.request.args.get(key)

class Test:
    def doSomething(self, request, param):
        sbxyz76680 = str(param)
        bar = sbxyz76680 + "_SafeStuff"
        return bar

@app.route("/xss-03/BenchmarkTest01772", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_get(request)

def do_get(request):
    return do_post(request)

def do_post(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    response.headers['X-XSS-Protection'] = '0'

    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest01772")

    bar = Test().doSomething(request, param)

    response.set_data(bar)
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
