
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02351", methods=['GET', 'POST'])
def benchmark_test_02351():
    if request.method == 'GET':
        return benchmark_test_02351_post()
    return benchmark_test_02351_post()

def benchmark_test_02351_post():
    response = make_response()
    param = ""
    flag = True
    names = request.args._get_wsgi_input()  # Retrieve request parameters
    for name in names:
        values = request.values.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02351":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    try:
        l = os.urandom(8).hex()  # Simulating SecureRandom
        remember_me_key = str(int(l, 16))

        user = "SafeLogan"
        full_class_name = benchmark_test_02351.__module__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key, cookie_val in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_val == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
            request.session[cookie_name] = remember_me_key
            response = remember_me

        response.data += "Weak Randomness Test os.urandom executed"
        return response
    except Exception as e:
        raise RuntimeError("Problem executing SecureRandom")

def do_something(param):
    a14991 = param
    b14991 = f"{a14991} SafeStuff"
    c14991 = b14991[:-1]
    e14991 = base64.b64decode(base64.b64encode(c14991.encode())).decode()  # B64 encode and decode
    f14991 = e14991.split(" ")[0]

    # Placeholder for calling external functionality
    # thing = ThingFactory.create_thing()
    # bar = thing.do_something(f14991)

    return f14991  # Placeholder return

if __name__ == "__main__":
    app.run(host='0.0.0.0')
