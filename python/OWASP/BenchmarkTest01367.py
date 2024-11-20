
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01367", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    param = request.args.get('BenchmarkTest01367', default='', type=str)

    bar = Test().do_something(request, param)

    try:
        random_bytes = bytearray(random.getrandbits(8) for _ in range(40))
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')
        
        user = "SafeByron"
        test_case_number = "01367"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            return "Welcome back: " + user + "<br/>"
        else:
            response = make_response(user + " has been remembered with cookie: " 
                                     + cookie_name + " whose value is: " 
                                     + remember_me_key + "<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'] = remember_me_key
            return response
    except Exception as e:
        print("Problem executing random number generation - TestCase")
        raise
    
    finally:
        print("Randomness Test executed")

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
