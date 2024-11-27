
import os
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route('/pathtraver-01/BenchmarkTest00952', methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = app.response_class(content_type='text/html;charset=UTF-8')
        user_cookie = ('BenchmarkTest00952', 'FileName', {'max_age': 60 * 3, 'secure': True, 'path': request.path, 'domain': request.host})
        response.set_cookie(*user_cookie)
        return render_template("pathtraver-01/BenchmarkTest00952.html")

    if request.method == 'POST':
        response = app.response_class(content_type='text/html;charset=UTF-8')
        the_cookies = request.cookies

        param = "noCookieValueSupplied"
        if 'BenchmarkTest00952' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00952'])

        bar = Test().do_something(request, param)

        start_uri_slashes = "//" if os.name == "posix" else "/"

        try:
            file_target = os.path.join(
                start_uri_slashes,
                os.path.normpath(os.path.expandvars(os.environ.get('TESTFILES_DIR', ''))).replace(' ', '_'),
                bar
            )
            response_data = f"Access to file: '{file_target}' created."
            if os.path.exists(file_target):
                response_data += " And file already exists."
            else:
                response_data += " But file doesn't exist yet."
            response.set_data(response_data)
        except Exception as e:
            raise Exception(e)

        return response

class Test:

    def do_something(self, request, param):
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target in ['B', 'C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
