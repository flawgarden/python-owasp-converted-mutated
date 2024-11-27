
from flask import Flask, request, render_template, make_response
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "path/to/testfiles/"  # Define the path to your test files

@app.route("/pathtraver-01/BenchmarkTest00955", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-01/BenchmarkTest00955.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00955", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie(user_cookie)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if 'BenchmarkTest00955' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00955'])

        bar = Test().do_something(param)

        file_name = os.path.join(TESTFILES_DIR, bar)

        try:
            # Note: This part should create a file for testing; adjust the logic as necessary
            # with open(file_name, 'a') as f:
            #     pass

            return "Now ready to write to file: {}".format(urllib.parse.quote(file_name))

        except Exception as e:
            print("Couldn't open FileOutputStream on file: '{}'".format(file_name))

class Test:

    def do_something(self, param):
        bar = ""
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
