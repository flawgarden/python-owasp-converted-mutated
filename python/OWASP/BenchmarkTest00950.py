
from flask import Flask, request, render_template
import os
from urllib.parse import unquote

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-01/BenchmarkTest00950", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = app.make_response(render_template("pathtraver-01/BenchmarkTest00950.html"))
        user_cookie = ('BenchmarkTest00950', 'FileName', {'max_age': 60 * 3, 'secure': True, 'path': request.path, 'domain': request.host})
        response.set_cookie(*user_cookie)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        cookies = request.cookies
        if cookies:
            param = cookies.get("BenchmarkTest00950", param)

        bar = Test().do_something(request, param)

        file_target = os.path.join(bar, "Test.txt")
        response_str = "Access to file: '" + file_target + "' created."
        if os.path.exists(file_target):
            response_str += " And file already exists."
        else:
            response_str += " But file doesn't exist yet."
        
        return response_str

class Test:
    def do_something(self, request, param):
        bar = param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
