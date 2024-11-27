
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = '/path/to/test/files/'

@app.route("/pathtraver-01/BenchmarkTest01111", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Language", "Accept-Encoding", "Connection"]:
            continue  # Skip standard headers
        param = name  # Grabs the first non-standard header name as the parameter
        break

    bar = Test().do_something(param)

    file_name = os.path.join(TESTFILES_DIR, bar)

    try:
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return f"The beginning of file: '{html_escape(file_name)}' is:<br><br>" + \
                   f"{html_escape(b.decode('utf-8', errors='ignore'))}"
    except Exception:
        print(f"Couldn't open file: '{file_name}'")
        return "An error occurred while trying to read the file."

class Test:

    @staticmethod
    def do_something(param):
        bar = ""
        num = 196
        if (500 // 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

def html_escape(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
