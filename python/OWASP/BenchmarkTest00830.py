
import os
import random
import urllib.parse
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00830", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest00830="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return response, "getQueryString() couldn't find expected parameter 'BenchmarkTest00830' in query string."

    param = query_string[param_loc + len(paramval):]  
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = None
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    try:
        stuff = random.SystemRandom().gauss(0, 1)
        remember_me_key = str(stuff)[2:]

        user = "SafeGayle"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.session.get(cookie_name):
                        found_user = True

        if found_user:
            response.get_data().decode("utf-8")
            response.data += "Welcome back: " + user + "<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
            request.session[cookie_name] = remember_me_key
            response.data += (
                user
                + " has been remembered with cookie: "
                + cookie_name
                + " whose value is: "
                + remember_me_key
                + "<br/>"
            )
    except Exception as e:
        print("Problem executing random.gauss() - TestCase")
        raise

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
