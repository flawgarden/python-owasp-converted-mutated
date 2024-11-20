
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01835", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-02/BenchmarkTest01835.html"))
        user_cookie = request.cookies.get('BenchmarkTest01835', 'FileName')
        response.set_cookie('BenchmarkTest01835', user_cookie, max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01835' in the_cookies:
            param = the_cookies['BenchmarkTest01835']

        bar = do_something(param)
        file_target = os.path.join('testfiles', bar)

        response_text = f"Access to file: '{file_target}' created."
        response_text += " And file already exists." if os.path.exists(file_target) else " But file doesn't exist yet."
        return response_text

def do_something(param):
    bar = param
    num = 196
    if (500 / 42) + num > 200:
        return bar
    else:
        return "This should never happen"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
