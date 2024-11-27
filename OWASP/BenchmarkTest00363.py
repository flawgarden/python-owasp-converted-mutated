
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'path/to/testfiles/'  # Specify the directory for test files

@app.route("/pathtraver-00/BenchmarkTest00363", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get('BenchmarkTest00363', "")
    bar = param
    file_name = os.path.join(TESTFILES_DIR, bar)

    try:
        with open(file_name, 'wb') as fos:
            return f"Now ready to write to file: {file_name}"
    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
        return "Failed to open file"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
