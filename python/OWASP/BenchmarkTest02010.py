
from flask import Flask, request, make_response, render_template
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-04/BenchmarkTest02010", methods=['GET', 'POST'])
def benchmark_test():
    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    for name in request.headers:
        if name in ['Accept', 'User-Agent', 'Host', 'Content-Type']:  # Add standard headers here
            continue  # If standard header, move on to next one

        param = name  # Grabs the name of the first non-standard header as the parameter value
        break

    bar = do_something(param)

    try:
        rand = random.getrandbits(64) / 2**64
        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front

        user = "SafeDonna"
        test_case_number = "02010"
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise e

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response


def do_something(param):
    bar = "This_should_always_happen" if (7 * 18 + 106) > 200 else param
    return bar


if __name__ == '__main__':
    app.run(host='0.0.0.0')
