
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01749", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest01749")
    bar = Test().do_something(request, param)

    file_name = None
    fis = None

    try:
        file_name = os.path.join('testfiles/', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response.set_data(
                f"The beginning of file: '{escape(file_name)}' is:\n\n" +
                escape(b.decode('utf-8', errors='ignore'))
            )
    except Exception as e:
        print(f"Couldn't open FileInputStream on file: '{file_name}'")
        response.set_data(
            "Problem getting FileInputStream: " + escape(str(e))
        )
    
    return response

class Test:
    def do_something(self, request, param):
        bar = None
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
