
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-03/BenchmarkTest01545", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return do_post(request)
    return do_get(request)


def do_get(request):
    return do_post(request)


def do_post(request):
    response = make_response()
    param = request.args.get("BenchmarkTest01545", "")

    bar = Test().do_something(request, param)

    try:
        stuff = random.SystemRandom().gauss(0, 1)
        remember_me_key = str(stuff)[2:]

        user = "SafeGayle"
        full_class_name = 'BenchmarkTest01545'
        test_case_number = full_class_name.split("BenchmarkTest")[-1]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response("")
            remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True)
            request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextGaussian() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    response.content_type = "text/html;charset=UTF-8"
    return response


class Test:

    def do_something(self, request, param):
        a43050 = param
        b43050 = list(a43050)
        b43050.append(" SafeStuff")
        b43050 = ''.join(b43050)[:-1] + "Chars"
        map43050 = {"key43050": b43050}
        c43050 = map43050["key43050"]
        d43050 = c43050[:-1]
        e43050 = base64.b64encode(base64.b64decode(d43050.encode())).decode()
        f43050 = e43050.split(" ")[0]
        thing = ThingFactory.create_thing()
        g43050 = "barbarians_at_the_gate"
        bar = thing.do_something(g43050)
        return bar


class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()


class ThingInterface:
    def do_something(self, input):
        return input


if __name__ == "__main__":
    app.run(host='0.0.0.0')
