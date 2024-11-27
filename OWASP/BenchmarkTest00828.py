
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00828", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00828="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval}' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    bar = param
    if param and len(param) > 1:
        bar = param[:-1]

    try:
        random_bytes = random.SystemRandom().getrandbits(320).to_bytes(40, 'big')
        remember_me_key = base64.b64encode(random_bytes).decode()

        user = "SafeBystander"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_name in cookies:
                if cookie_name == f"rememberMe{test_case_number}":
                    if cookies[cookie_name] == request.environ.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing random number generation")
        raise

    response.data += "Randomness Test executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
