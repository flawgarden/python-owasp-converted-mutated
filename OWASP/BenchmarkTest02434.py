
from flask import Flask, request, render_template, make_response
import os
import random
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-05/BenchmarkTest02434", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response("")
    param = request.args.get("BenchmarkTest02434", "")
    bar = do_something(param)

    try:
        random_bytes = bytearray(40)
        get_next_number(random_bytes)

        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        test_case_number = "02434"
        user += test_case_number
        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data += b"Welcome back: " + user.encode() + b"<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data += (user + " has been remembered with cookie: " +
                              cookie_name + " whose value is: " +
                              remember_me_key + "<br/>").encode()
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e
    finally:
        response.data += b"Randomness Test executed<br/>"

    return response


def get_next_number(byte_array):
    random.SystemRandom().getrandbits(8 * len(byte_array))


def do_something(param):
    bar = "safe!"
    map_29737 = {
        "keyA-29737": "a-Value",
        "keyB-29737": param,
        "keyC": "another-Value"
    }
    bar = map_29737.get("keyB-29737", "")
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
