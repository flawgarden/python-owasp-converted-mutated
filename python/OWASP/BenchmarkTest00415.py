
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00415", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    param = request.args.get("BenchmarkTest00415", "")
    
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    try:
        rand = random.Random().random()  # Simulating SecureRandom
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True

        response = make_response()
        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.request'].set_wsgi_headers({'Set-Cookie': response.headers['Set-Cookie']})
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        
        response.data += "Weak Randomness Test executed"
        return response

    except Exception as e:
        print("Problem executing random generation - TestCase")
        raise e

if __name__ == "__main__":
    app.run(host='0.0.0.0')
