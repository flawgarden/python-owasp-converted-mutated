
from flask import Flask, request, make_response, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-05/BenchmarkTest02473", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    values = request.values.getlist("BenchmarkTest02473")
    param = values[0] if values else ""

    bar = do_something(param)

    value = random.random()
    remember_me_key = str(value)[2:]  # Trim off the 0. at the front.

    user = "Doug"
    full_class_name = benchmark_test.__module__ + "." + benchmark_test.__qualname__
    test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = f'rememberMe{test_case_number}'

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, cookie in cookies.items():
            if cookie_name == key:
                if cookie == request.cookies.get(cookie_name):
                    found_user = True
                    break

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        remember_me = make_response()
        remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True,
                                domain=urllib.parse.urlparse(request.url).netloc,
                                path=request.path)
        request.environ['werkzeug.request'].session[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.random() executed"
    return response


def do_something(param):
    bar = "safe!"
    map_91880 = {
        "keyA-91880": "a-Value",
        "keyB-91880": param,
        "keyC": "another-Value"
    }
    bar = map_91880.get("keyB-91880")  # get it back out

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
