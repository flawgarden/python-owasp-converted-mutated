
import os
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/pathtraver-01/BenchmarkTest00951", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-01/BenchmarkTest00951.html"))
        user_cookie = "BenchmarkTest00951"
        response.set_cookie(user_cookie, "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if the_cookies:
            for cookie_name, cookie_value in the_cookies.items():
                if cookie_name == "BenchmarkTest00951":
                    param = urllib.parse.unquote(cookie_value)
                    break
        
        bar = Test().do_something(request, param)

        start_uri_slashes = "/" if os.name == "nt" else "//"
        file_uri = f"file:{start_uri_slashes}{os.path.normpath('testfiles').replace(' ', '_')}/{bar}"

        file_target = os.path.abspath(file_uri)

        output = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            output += " And file already exists."
        else:
            output += " But file doesn't exist yet."

        return output


class Test:
    def do_something(self, request, param):
        bar = param
        num = 106
        bar = "This_should_always_happen" if (7 * 18) + num > 200 else param
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
