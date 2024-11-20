
from flask import Flask, request, make_response, render_template
import random

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-05/BenchmarkTest02246", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    map = request.args.to_dict()
    param = ""
    if map:
        values = map.get("BenchmarkTest02246")
        if values:
            param = values[0]

    bar = do_something(request, param)

    rand_number = random.randint(0, 98)
    remember_me_key = str(rand_number)

    user = "Inga"
    full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
    test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie == cookie_name:
                if cookies[cookie] == request.cookies.get(cookie_name):
                    found_user = True

    if found_user:
        return f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
        return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += b"Weak Randomness Test random.randint(0, 98) executed"
    return response


def do_something(request, param):
    bar = "safe!"
    map19712 = {}
    map19712["keyA-19712"] = "a-Value"  # put some stuff in the collection
    map19712["keyB-19712"] = param  # put it in a collection
    map19712["keyC"] = "another-Value"  # put some stuff in the collection
    bar = map19712["keyB-19712"]  # get it back out

    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
