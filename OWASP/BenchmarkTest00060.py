
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = 'testfiles'  # Change this to your actual test files directory

@app.route("/pathtraver-00/BenchmarkTest00060", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00060.html"))
        user_cookie = ('BenchmarkTest00060', 'FileName', {'secure': True, 'max_age': 60 * 3, 'path': request.path, 'domain': request.host})
        response.set_cookie(*user_cookie)
        return response

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"

        if 'BenchmarkTest00060' in cookies:
            param = cookies['BenchmarkTest00060']

        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()

        file_target = os.path.join(TESTFILES_DIR, bar)
        output = f"Access to file: '{file_target}' created."

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
