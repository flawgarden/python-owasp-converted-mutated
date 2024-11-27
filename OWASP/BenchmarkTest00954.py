
import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-01/BenchmarkTest00954", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-01/BenchmarkTest00954.html"))
        user_cookie = make_response("Cookie Set")
        user_cookie.set_cookie("BenchmarkTest00954", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest00954", value="FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if "BenchmarkTest00954" in the_cookies:
            param = unquote(the_cookies["BenchmarkTest00954"])

        bar = Test().do_something(param)
        file_name = os.path.join("path_to_test_files", bar)

        try:
            with open(file_name, 'wb') as fos:
                return f"Now ready to write to file: {file_name}"

        except Exception as e:
            print(f"Couldn't open FileOutputStream on file: '{file_name}'")

class Test:

    def do_something(self, param):
        bar = "safe!"
        map9749 = {
            "keyA-9749": "a_Value",
            "keyB-9749": param,
            "keyC": "another_Value"
        }
        bar = map9749["keyB-9749"]
        bar = map9749["keyA-9749"]

        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
