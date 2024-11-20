
import os
from flask import Flask, request, render_template, make_response, redirect, url_for
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest00949", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-01/BenchmarkTest00949.html"))
        user_cookie = make_response(" ")
        user_cookie.set_cookie("BenchmarkTest00949", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest00949", "FileName", max_age=60 * 3, secure=True)
        response = redirect(url_for('benchmark_test', _external=True))
        return response

    param = "noCookieValueSupplied"
    the_cookies = request.cookies
    if 'BenchmarkTest00949' in the_cookies:
        param = urllib.parse.unquote(the_cookies['BenchmarkTest00949'])

    bar = Test().do_something(request, param)

    file_target = os.path.join('path/to/testfiles', bar)
    
    output = f"Access to file: '{file_target}' created."
    if os.path.exists(file_target):
        output += " And file already exists."
    else:
        output += " But file doesn't exist yet."
    
    return output

class Test:
    def do_something(self, request, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
