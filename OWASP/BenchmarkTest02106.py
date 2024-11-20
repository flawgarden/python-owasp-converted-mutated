
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02106", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02106", "")
    bar = do_something(param)

    file_target = bar
    response += "Access to file: '" + html_encode(file_target) + "' created.<br>"

    if os.path.exists(file_target):
        response += " And file already exists.<br>"
    else:
        response += " But file doesn't exist yet.<br>"

    return response

def do_something(param):
    bar = ""
    if param:
        bar = base64_decode(base64_encode(param))
    return bar

def base64_encode(data):
    import base64
    return base64.b64encode(data.encode()).decode()

def base64_decode(data):
    import base64
    return base64.b64decode(data).decode()

def html_encode(data):
    from markupsafe import escape
    return escape(data)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
