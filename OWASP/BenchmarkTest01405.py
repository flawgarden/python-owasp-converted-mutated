
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest01405", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_content = ""
    param = ""
    flag = True
    names = request.args.to_dict()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01405":
                    param = name
                    flag = False

    bar = Test().do_something(param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join("TESTFILES_DIR", bar)  # Set your TESTFILES_DIR appropriately
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response_content += f"The beginning of file: '{html_encode(file_name)}' is:\n\n{html_encode(b.decode())}"
    except Exception as e:
        response_content += f"Couldn't open FileInputStream on file: '{file_name}'"
        response_content += f"Problem getting FileInputStream: {html_encode(str(e))}"

    return render_template("response.html", response=response_content)

class Test:

    def do_something(self, param):
        bar = param
        return bar

def html_encode(value):
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
