
import os
from flask import Flask, request, render_template
from urllib.parse import quote, unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest02378", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest02378", "")
    bar = do_something(param)

    startURIslashes = "/" if os.name == 'nt' else "//"

    try:
        file_uri = f"file:{startURIslashes}{quote(os.path.join('testfiles', bar.replace(' ', '_')))}"
        file_target = os.path.abspath(file_uri.replace("file:", "").replace("/", os.sep))

        response.data = f"Access to file: '{file_target}' created.<br>"
        if os.path.exists(file_target):
            response.data += " And file already exists.<br>"
        else:
            response.data += " But file doesn't exist yet.<br>"
    except Exception as e:
        raise Exception(e)

    return response

def do_something(param):
    thing = create_thing()
    bar = thing.do_something(param)

    return bar

def create_thing():
    return ThingInterface()

class ThingInterface:
    def do_something(self, param):
        # Simulated processing for the example
        return param[::-1]  # Just as an example, reverse the string

if __name__ == "__main__":
    app.run(host='0.0.0.0')
