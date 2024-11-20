
import os
import random
import base64
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = "your_secret_key_here"

@app.route("/weakrand-01/BenchmarkTest00578", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00578":
                    param = name
                    flag = False

    thing = create_thing()
    bar = thing.do_something(param)

    try:
        num_gen = random.SystemRandom()

        # Get 40 random bytes
        random_bytes = bytearray(40)
        get_next_number(num_gen, random_bytes)

        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise

    response.data += "Randomness Test executed"
    return response

def get_next_number(generator, barray):
    for i in range(len(barray)):
        barray[i] = generator.randint(0, 255)

def create_thing():
    class Thing:
        def do_something(self, param):
            return f"Processed {param}"

    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
