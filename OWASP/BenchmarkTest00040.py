
import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00040", methods=['GET', 'POST'])
def benchmark_test_00040():
    if request.method == 'GET':
        return benchmark_test_00040_post()
    return benchmark_test_00040_post()

def benchmark_test_00040_post():
    response = "Access to file: '"
    param = request.args.get('BenchmarkTest00040', '')

    file_target = os.path.abspath(param)
    response += f"{file_target}' created."

    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
