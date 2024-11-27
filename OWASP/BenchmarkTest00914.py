
import os
import random
import base64
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)
app.config['DEBUG'] = True


@app.route("/weakrand-02/BenchmarkTest00914", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get("BenchmarkTest00914", "")

    bar = escape_for_html(param)

    try:
        num_gen = random.SystemRandom()

        # Get 40 random bytes
        random_bytes = num_gen.getrandbits(40 * 8).to_bytes(40, byteorder='big')
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        full_class_name = "BenchmarkTest00914"
        test_case_number = full_class_name.split("BenchmarkTest")[-1]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        if 'cookies' in request.cookies:
            cookies = request.cookies
            if cookie_name in cookies:
                if cookies[cookie_name] == session.get(cookie_name):
                    found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom - TestCase")
        raise e
    finally:
        response.data += "Randomness Test executed"

    return response


def escape_for_html(value):
    return value  # Add an actual HTML escape implementation if necessary


if __name__ == "__main__":
    app.run(host='0.0.0.0')
