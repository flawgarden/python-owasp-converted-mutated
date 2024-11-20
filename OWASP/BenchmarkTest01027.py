
from flask import Flask, request, render_template
import urllib.parse
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01027", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01027", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    file_target = os.path.abspath(bar)
    response_text = f"Access to file: '{html_escape(file_target)}' created."

    if os.path.exists(file_target):
        response_text += " And file already exists."
    else:
        response_text += " But file doesn't exist yet."

    return response_text

class Test:
    def do_something(self, request, param):
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
