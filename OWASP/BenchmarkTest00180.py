
from flask import Flask, request, make_response, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00180", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest00180", "")
    param = urllib.parse.unquote(param)

    bar = ""
    
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    try:
        rand = get_next_number()
        remember_me_key = str(rand)[2:]

        user = "SafeDonatella"
        test_case_number = "BenchmarkTest00180"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie_key, cookie_value in cookies.items():
                if cookie_name == cookie_key:
                    if cookie_value == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = (f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        
    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise e

    response.data += "Weak Randomness Test executed"
    return response


def get_next_number():
    return random.SystemRandom().random()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
