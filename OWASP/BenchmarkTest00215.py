
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "./testfiles"  # Update this path as necessary

@app.route("/pathtraver-00/BenchmarkTest00215", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Encoding"]:  # Add any common headers to ignore
            continue  # If standard header, move on to next one

        param = name  # Grabs the name of the first non-standard header as the parameter value
        break

    bar = param

    file_target = os.path.join(TESTFILES_DIR, bar)
    output = "Access to file: '{} created.".format(file_target)
    
    if os.path.exists(file_target):
        output += " And file already exists."
    else:
        output += " But file doesn't exist yet."

    return output

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
