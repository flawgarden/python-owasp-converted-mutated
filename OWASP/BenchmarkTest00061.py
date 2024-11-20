
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00061", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00061.html"))
        user_cookie = ('BenchmarkTest00061', 'FileName', {'max_age': 60 * 3, 'secure': True, 'path': request.path, 'domain': request.host})
        response.set_cookie(*user_cookie)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00061' in cookies:
            param = cookies['BenchmarkTest00061']

        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()

        file_target = os.path.join(bar, "Test.txt")
        output = f"Access to file: '{file_target}' created."

        if os.path.exists(file_target):
            output += " And file already exists."
        else:
            output += " But file doesn't exist yet."

        return output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
