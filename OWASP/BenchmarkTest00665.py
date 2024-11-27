
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-01/BenchmarkTest00665", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.values.get("BenchmarkTest00665", "")
    
    bar = param if (7 * 42) - 106 <= 200 else "This should never happen"

    try:
        stuff = random.SystemRandom().gauss(0, 1)
        remember_me_key = str(stuff)[2:]  # Trim off the 0. at the front.

        user = "SafeGayle"
        test_case_number = "00665"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_cookie(cookie_name, remember_me_key)
            response.data = (
                f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            )

    except Exception as e:
        print("Problem executing random.gauss() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.gauss() executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
