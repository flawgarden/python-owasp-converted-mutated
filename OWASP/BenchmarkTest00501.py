
import os
import random
import base64
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key_here'

@app.route("/weakrand-01/BenchmarkTest00501", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.values.get("BenchmarkTest00501", "")

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        del values_list[0]  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    try:
        random_bytes = bytearray(random.getrandbits(8) for _ in range(40))
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = type(app).__module__ + "." + type(app).__name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for key, value in cookies.items():
                if key == cookie_name:
                    if value == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.full_path)
            session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print(f"Problem executing SecureRandom.nextBytes() - TestCase: {e}")

    response.data += "Randomness Test executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
