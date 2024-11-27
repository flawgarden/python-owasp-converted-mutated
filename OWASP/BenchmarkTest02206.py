
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-02/BenchmarkTest02206", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"

    param = request.args.get('BenchmarkTest02206', '')

    bar = do_something(param)

    file_name = os.path.join('testfiles', bar)
    content = ""

    try:
        with open(file_name, 'r') as file:
            content = file.read(1000)
            response_body = f"The beginning of file: '{escape(file_name)}' is:\n\n"
            response_body += escape(content)
            return response_body
    except Exception as e:
        print(f"Couldn't open InputStream on file: '{file_name}'")
        return f"Problem getting InputStream: {escape(str(e))}"

def do_something(param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

def escape(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
