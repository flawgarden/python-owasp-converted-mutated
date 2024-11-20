
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01642", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01642="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01642' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    file_target = os.path.join("path_to_test_files", bar)
    response = "Access to file: '{}' created.".format(escape_html(file_target))
    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."
    
    return response

class Test:

    def do_something(self, param):
        thing = create_thing()
        bar = thing.do_something(param)
        return bar

def escape_html(text):
    return urllib.parse.quote(text)

def create_thing():
    # Replace this with actual object creation logic.
    return ThingInterface()

class ThingInterface:
    def do_something(self, param):
        # Implement the logic similar to the Java version.
        return param  # Placeholder for actual logic.

if __name__ == "__main__":
    app.run(host='0.0.0.0')
