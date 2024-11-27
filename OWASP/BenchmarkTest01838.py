
from flask import Flask, request, render_template, make_response
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01838", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("pathtraver-02/BenchmarkTest01838.html"))
        user_cookie = make_response('FileName')
        user_cookie.set_max_age(60 * 3)  # Store cookie for 3 minutes
        user_cookie.set_secure(True)
        user_cookie.set_path(request.path)
        user_cookie.set_domain(request.host)
        response.set_cookie("BenchmarkTest01838", "FileName")
        response.mimetype = "text/html;charset=UTF-8"
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if "BenchmarkTest01838" in the_cookies:
            param = the_cookies["BenchmarkTest01838"]

        bar = do_something(request, param)
        file_name = os.path.join("path_to_test_files", bar)
        
        try:
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                return f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8')}"
        except Exception as e:
            return f"Problem getting FileInputStream: {str(e)}"

def do_something(request, param):
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
