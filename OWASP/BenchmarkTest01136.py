
import os
import random
import base64
from flask import Flask, request, render_template, session, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'super_secret_key'

@app.route("/weakrand-02/BenchmarkTest01136", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    for name in request.headers:
        if name in common_headers():
            continue  # If standard header, move on to next one
        param = name
        break

    bar = Test().do_something(param)

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = type(request).__module__ + "." + type(request).__qualname__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie_name] == session.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            session[cookie_name] = remember_me_key
            response.data = (f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>").encode('utf-8')

    except Exception as e:
        print("Problem executing random byte generation - TestCase")
        raise e

    response.data += b"Randomness Test os.urandom() executed"
    return response


class Test:
    def do_something(self, param):
        a58606 = param
        b58606 = a58606 + " SafeStuff"
        b58606 = b58606[:-5] + "Chars"
        map58606 = {"key58606": b58606}
        c58606 = map58606["key58606"]
        d58606 = c58606[:-1]
        e58606 = base64.b64decode(base64.b64encode(d58606.encode())).decode()
        f58606 = e58606.split(" ")[0]

        thing = create_thing()
        g58606 = "barbarians_at_the_gate"
        bar = thing.do_something(g58606)

        return bar


def common_headers():
    return ["Content-Type", "User-Agent", "Accept"]

def create_thing():
    # Replace this function with the actual implementation
    class Thing:
        def do_something(self, data):
            return f"Processed {data}"

    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
