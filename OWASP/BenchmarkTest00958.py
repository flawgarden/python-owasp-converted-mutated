
from flask import Flask, request, render_template, make_response
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest00958", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("pathtraver-01/BenchmarkTest00958.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest00958", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        resp.set_cookie("BenchmarkTest00958", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return resp

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"

        if "BenchmarkTest00958" in cookies:
            param = urllib.parse.unquote(cookies["BenchmarkTest00958"])

        bar = Test().do_something(request, param)

        file_name = os.path.join("path/to/test/files/", bar)

        try:
            with open(file_name, 'rb') as f:
                b = f.read(1000)
                return f"The beginning of file: '{file_name}' is:\n\n{b.decode()}"
        except Exception as e:
            return f"Couldn't open InputStream on file: '{file_name}'. Problem getting InputStream: {str(e)}"

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_ = {
            "keyA-37053": "a_Value",
            "keyB-37053": param,
            "keyC": "another_Value"
        }
        bar = map_.get("keyB-37053")
        bar = map_.get("keyA-37053")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
