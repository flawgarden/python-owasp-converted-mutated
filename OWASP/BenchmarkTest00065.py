
import os
import base64
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['TESTFILES_DIR'] = 'path/to/testfiles/'  # Update with the correct path

@app.route("/pathtraver-00/BenchmarkTest00065", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-00/BenchmarkTest00065.html"))
        user_cookie = ('BenchmarkTest00065', 'FileName', 60 * 3)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host.split(':')[0])
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest00065' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00065'])

        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()

        file_name = os.path.join(app.config['TESTFILES_DIR'], bar)
        try:
            with open(file_name, 'rb') as f:
                b = f.read(1000)
                return "The beginning of file: '{}' is:\n\n{}".format(urllib.parse.quote(file_name), urllib.parse.quote(b.decode()))
        except Exception as e:
            return "Couldn't open InputStream on file: '{}'".format(file_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
