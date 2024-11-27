
import os
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'  # Needed for session management

@app.route("/weakrand-05/BenchmarkTest02520", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    values = request.values.getlist("BenchmarkTest02520")
    param = values[0] if values else ""

    bar = do_something(param)

    try:
        rand = random.SystemRandom().random()
        remember_me_key = str(rand)[2:]

        user = "SafeDonna"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie == cookie_name:
                    if cookies[cookie] == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response = remember_me

    except Exception as e:
        print("Problem executing SecureRandom.random() - TestCase")
        raise e
    
    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

def do_something(param):
    bar = ''
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
