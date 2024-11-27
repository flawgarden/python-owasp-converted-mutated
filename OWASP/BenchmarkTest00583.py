
import os
import random
import base64
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['SECRET_KEY'] = os.urandom(24)
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00583", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""
    flag = True
    
    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00583":
                    param = name
                    flag = False

    bar = escape_html(param)

    try:
        random_bytes = bytearray(random.getrandbits(8) for _ in range(40))
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        test_case_number = "00583"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_name in cookies:
                cookie_value = cookies[cookie_name]
                if cookie_name == cookie_name:
                    if cookie_value == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        response.data = str(e)

    response.data += "Randomness Test executed"
    return response

def escape_html(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
