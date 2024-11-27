
import os
import urllib
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "path/to/test/files/"  # Update this to the correct path for test files

@app.route("/pathtraver-01/BenchmarkTest00953", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-01/BenchmarkTest00953.html"))
        user_cookie = ('BenchmarkTest00953', 'FileName', 60 * 3, '/', request.host)
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], path=user_cookie[3], domain=user_cookie[4], secure=True)
        return response
    else:
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00953' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest00953'])

        bar = Test().do_something(request, param)
        file_name = os.path.join(TESTFILES_DIR, bar)

        try:
            with open(file_name, 'w') as fos:
                fos.write("Now ready to write to file: " + file_name)

        except Exception as e:
            print("Couldn't open FileOutputStream on file: '" + file_name + "'")

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ['safe', param, 'moresafe']
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
