
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Set a secret key for session management

@app.route("/weakrand-02/BenchmarkTest01274", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get("BenchmarkTest01274", "")

    bar = Test().do_something(request, param)

    rand_number = random.randint(0, 98)
    remember_me_key = str(rand_number)

    user = "Inga"
    full_class_name = __name__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == session.get(cookie_name):
                    found_user = True

    if found_user:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        session[cookie_name] = remember_me_key
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")
        response.headers.add('Set-Cookie', remember_me)

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test random.randint(0, 98) executed")
    return response

class Test:

    def do_something(self, request, param):
        bar = param
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
