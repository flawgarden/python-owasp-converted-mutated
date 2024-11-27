
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-03/BenchmarkTest01694", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01694="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01694' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = request.args.get('BenchmarkTest01694')

    bar = Test().do_something(param)

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_name, cookie_value in cookies.items():
                if cookie_name == cookie_name:
                    if cookie_value == str(request.cookies.get(cookie_name)):
                        found_user = True

        if found_user:
            response.data = "Welcome back: " + user + "<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.session[cookie_name] = remember_me_key
            response.data = user + " has been remembered with cookie: " + cookie_name + " whose value is: " + remember_me_key + "<br/>"
    except Exception as e:
        print("Problem executing random bytes generation - TestCase")
        raise

    response.data += "Randomness Test executed"
    return response


class Test:

    def do_something(self, param):
        return param.replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
