
from flask import Flask, request, make_response
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-04/BenchmarkTest02061", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.getlist("BenchmarkTest02061")

    if headers:
        param = headers[0]  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    r = random.randint(0, 2147483647)
    remember_me_key = str(r)

    user = "Ingrid"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies[cookie_name]:
                found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['wsgi.session'][cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test random.randint() executed"
    return response


def do_something(request, param):
    num = 106
    return param if (7 * 42) - num <= 200 else "This should never happen"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
