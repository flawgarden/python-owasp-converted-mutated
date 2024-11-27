
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01677", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01677="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01677' in query string."

    param = query_string[param_loc + len(paramval):]  
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param

    bar = Test().do_something(request, param)

    rand = random.random()
    remember_me_key = str(rand)[2:] 

    user = "Floyd"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies

    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
        request.session[cookie_name] = remember_me_key
        remember_me.set_data(user + " has been remembered with cookie: " + cookie_name +
                              " whose value is: " + remember_me_key + "<br/>")
        return remember_me.get_data() + "Weak Randomness Test executed"

class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0) 
            bar = values_list[0]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
