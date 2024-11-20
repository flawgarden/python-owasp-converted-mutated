
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00629", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get('BenchmarkTest00629', '')
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    file_name = os.path.join('testfiles', secure_filename(bar))

    try:
        with open(file_name, 'r') as file:
            b = file.read(1000)
            return render_template("result.html", file_name=file_name, content=b)
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return render_template("error.html", error_message=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
