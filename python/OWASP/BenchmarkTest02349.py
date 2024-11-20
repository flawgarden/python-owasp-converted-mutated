
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02349", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = make_response()
    
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values and flag:
            for value in values:
                if value == "BenchmarkTest02349":
                    param = name
                    flag = False

    bar = do_something(request, param)

    rand_number = random.SystemRandom().randint(0, 99)
    remember_me_key = str(rand_number)

    user = "SafeInga"
    test_case_number = "02349"

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie_name, cookie_value in cookies.items():
            if cookie_name == cookie_name:
                if cookie_value == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response.set_data("Welcome back: " + user + "<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, httponly=True, secure=True)
        request.environ['werkzeug.session'].setcookie(cookie_name, remember_me_key)
        response.set_data(user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")

    return response

def do_something(request, param):
    a55770 = param
    b55770 = a55770 + " SafeStuff"
    b55770 = b55770[:-5] + "Chars"
    
    map55770 = {}
    map55770["key55770"] = b55770

    c55770 = map55770["key55770"]
    d55770 = c55770[:-1]
    e55770 = d55770.encode('utf-8').decode('utf-8')
    f55770 = e55770.split(" ")[0]
    
    thing = create_thing()
    bar = thing.do_something(f55770)

    return bar

def create_thing():
    class Thing:
        def do_something(self, input_str):
            return input_str + " processed"
    
    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
