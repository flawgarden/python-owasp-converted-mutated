
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01702", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        query_string = request.query_string.decode('utf-8')
        paramval = "BenchmarkTest01702="
        param_loc = query_string.find(paramval)

        if param_loc == -1:
            return "getQueryString() couldn't find expected parameter 'BenchmarkTest01702' in query string."

        param = query_string[param_loc + len(paramval):]
        ampersand_loc = query_string.find("&", param_loc)

        if ampersand_loc != -1:
            param = query_string[param_loc + len(paramval):ampersand_loc]

        param = param  # decode if needed, like urllib.parse.unquote(param)

        bar = Test().do_something(param)

        try:
            rand = random.SystemRandom().random()
            remember_me_key = str(rand)[2:]

            user = "SafeDonna"
            full_class_name = benchmark_test.__module__
            testcase_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

            user += testcase_number
            cookie_name = "rememberMe" + testcase_number

            found_user = False
            cookies = request.cookies

            if cookies:
                for cookie_name, cookie_value in cookies.items():
                    if cookie_name == cookie_name:
                        if cookie_value == request.cookies.get(cookie_name):
                            found_user = True

            if found_user:
                return f"Welcome back: {user}<br/>"
            else:
                response = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                request.environ['beaker.session'][cookie_name] = remember_me_key
                return response

        except Exception as e:
            print("Problem executing SecureRandom.nextDouble() - TestCase")
            return "Internal Server Error", 500

        return "Weak Randomness Test random.SystemRandom().random() executed"

class Test:
    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            bar = param[:-1]
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
