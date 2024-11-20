
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01029", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01029", "")

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    start_uri_slashes = ""
    if os.name == 'nt':
        start_uri_slashes = "/"
    else:
        start_uri_slashes = "//"

    try:
        file_uri = f"file:{start_uri_slashes}{os.path.join('testfiles', bar).replace(' ', '_')}"
        file_target = os.path.abspath(file_uri)

        response_message = f"Access to file: '{file_target}' created."

        if os.path.exists(file_target):
            response_message += " And file already exists."
        else:
            response_message += " But file doesn't exist yet."

        return response_message
    except Exception as e:
        return str(e)

class Test:
    def do_something(self, request, param):
        thing = create_thing()
        bar = thing.do_something(param)
        return bar

def create_thing():
    # The implementation of this function should return an object similar to
    # org.owasp.benchmark.helpers.ThingFactory.createThing()
    return ThingInterface()

class ThingInterface:
    def do_something(self, param):
        # Placeholder implementation
        return param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
