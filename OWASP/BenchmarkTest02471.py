
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-03/BenchmarkTest02471", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    
    values = request.values.getlist("BenchmarkTest02471")
    param = values[0] if values else ""

    bar = do_something(param)

    file_name = os.path.join('testfiles', bar)
    is_stream = None

    try:
        with open(file_name, 'rb') as is_stream:
            b = is_stream.read(1000)
            output = (
                "The beginning of file: '"
                + file_name
                + "' is:\n\n"
                + str(b, 'utf-8')
            )
            return render_template("index.html", output=output)
    except Exception as e:
        print("Couldn't open InputStream on file: '" + file_name + "'")
        return render_template("index.html", output="Problem getting InputStream: " + str(e))

def do_something(param):
    bar = ""

    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
