
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest01129", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name not in ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Connection', 
                        'Cookie', 'Host', 'User-Agent', 'Referer', 'Origin']:
            param = name
            break

    bar = Test().do_something(param)

    rand_number = os.urandom(1)[0] % 99
    remember_me_key = str(rand_number)

    user = "Inga"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__qualname__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True
                    break

    response = make_response()
    
    if found_user:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

class Test:
    def do_something(self, param):
        bar = ""
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
