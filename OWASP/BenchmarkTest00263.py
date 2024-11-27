
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00263", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ''
    param = ''
    headers = request.headers.getlist("BenchmarkTest00263")

    if headers and len(headers) > 0:
        param = headers[0]

    param = urllib.parse.unquote(param)

    bar = None
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    file_name = None
    try:
        file_name = os.path.join('path/to/testfiles', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response += f"The beginning of file: '{html_escape(file_name)}' is:\n\n"
            response += html_escape(b.decode('utf-8', errors='ignore'))
    except Exception as e:
        response += f"Couldn't open FileInputStream on file: '{file_name}'"
        response += f"Problem getting FileInputStream: {html_escape(str(e))}"

    return render_template("index.html", response=response)

def html_escape(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
