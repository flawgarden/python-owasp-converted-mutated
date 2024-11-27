
import os
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02001", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Encoding', 'Accept-Language']:  # commonHeaders example
            continue

        param = name  # Grabs the name of the first non-standard header as the parameter
        break

    bar = do_something(param)

    rand = os.urandom(4).hex()  # Simulating randomness
    remember_me_key = rand[2:] # Trim off the first two characters

    user = "Floyd"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if key == cookie_name:
                if value == request.args.get(cookie_name):
                    found_user = True

    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True)
        request.args[cookie_name] = remember_me_key
        response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

def do_something(param):
    return param  # Assuming we simplify the HTML escaping

if __name__ == "__main__":
    app.run(host='0.0.0.0')
