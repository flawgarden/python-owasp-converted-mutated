
import os
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest01236", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = "<html><body>"
    param = request.form.get("BenchmarkTest01236", "")
    
    bar = Test().do_something(request, param)

    start_uri_slashes = "//" if os.name != 'nt' else "/"
    
    try:
        file_uri = f"file:{start_uri_slashes}{urllib.parse.quote(os.path.normpath('testfiles_dir').replace(' ', '_'))}{bar}"
        file_target = os.path.normpath(file_uri)
        response += f"Access to file: '{html_escape(file_target)}' created.<br>"
        
        if os.path.exists(file_target):
            response += " And file already exists.<br>"
        else:
            response += " But file doesn't exist yet.<br>"
    except Exception as e:
        raise Exception("Error processing the file URI") from e

    response += "</body></html>"
    return response

class Test:
    def do_something(self, request, param):
        thing = self.create_thing()
        bar = thing.do_something(param)
        return bar

    def create_thing(self):
        return Thing()

class Thing:
    def do_something(self, param):
        # Implement the logic here for the mock implementation
        return param

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
