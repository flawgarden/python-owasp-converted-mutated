
from flask import Flask, request, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01681", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    elif request.method == 'POST':
        return benchmark_test_post(request)

def benchmark_test_post(request):
    response = ""
    query_string = request.query_string.decode("utf-8")
    paramval = "BenchmarkTest01681="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01681' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    remember_me_key = str(random.randint(0, 2**31 - 1))

    user = "Ingrid"
    full_class_name = benchmark_test.__module__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number
    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if cookie_name == key:
                if value == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        response += "Welcome back: " + user + "<br/>"
    else:
        remember_me = (cookie_name, remember_me_key)
        response += f"{user} has been remembered with cookie: {remember_me[0]} whose value is: {remember_me[1]}<br/>"

    response += "Weak Randomness Test executed"
    return response

class Test:
    
    def do_something(self, request, param):
        bar = "safe!"
        map_97890 = {
            "keyA-97890": "a_Value",
            "keyB-97890": param,
            "keyC": "another_Value"
        }
        bar = map_97890["keyB-97890"]
        bar = map_97890["keyA-97890"]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
