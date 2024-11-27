
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest00956", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-01/BenchmarkTest00956.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00956", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(":")[0])
        response.set_cookie("BenchmarkTest00956", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(":")[0])
        return response
        
    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest00956" in the_cookies:
            param = the_cookies["BenchmarkTest00956"]

        bar = Test().do_something(request, param)
        file_name = os.path.join("TESTFILES_DIR", bar)

        try:
            with open(file_name, 'a') as f:  # append mode
                return f"Now ready to write to file: {file_name}"

        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")
            return str(e)

class Test:
    def do_something(self, request, param):
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
