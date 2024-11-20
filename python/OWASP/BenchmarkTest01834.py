
import os
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01834", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-02/BenchmarkTest01834.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01834", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest01834", "FileName", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if 'BenchmarkTest01834' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01834'])

        bar = do_something(param)

        file_target = os.path.join('testfiles', bar)
        response_text = f"Access to file: '{file_target}' created."
        if os.path.exists(file_target):
            response_text += " And file already exists."
        else:
            response_text += " But file doesn't exist yet."
        return response_text

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
