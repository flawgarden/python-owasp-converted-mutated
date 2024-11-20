
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheValue(self, param_name):
        return self.request.args.get(param_name)

class ThingInterface:
    def doSomething(self, input_param):
        return input_param

class ThingFactory:
    @staticmethod
    def createThing():
        return ThingInterface()

@app.route("/pathtraver-00/BenchmarkTest00863", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    scr = SeparateClassRequest(request)
    param = scr.getTheValue("BenchmarkTest00863")

    thing = ThingFactory.createThing()
    bar = thing.doSomething(param)

    file_target = os.path.join(bar, "Test.txt")
    response.set_data(f"Access to file: '{file_target}' created.<br>")

    if os.path.exists(file_target):
        response.set_data(response.get_data(as_text=True) + " And file already exists.<br>")
    else:
        response.set_data(response.get_data(as_text=True) + " But file doesn't exist yet.<br>")

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
