
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-02/BenchmarkTest00989", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("weakrand-02/BenchmarkTest00989.html"))
        user_cookie = make_response('whatever', 200)
        user_cookie.set_cookie('BenchmarkTest00989', 'whatever', max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie('BenchmarkTest00989', value='whatever', max_age=60 * 3, secure=True)
        return response

    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00989' in the_cookies:
            param = the_cookies['BenchmarkTest00989']

        bar = Test().do_something(request, param)

        try:
            rand_number = random.randint(0, 98)
            remember_me_key = str(rand_number)

            user = "SafeInga"
            full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
            test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

            user += test_case_number
            cookie_name = "rememberMe" + test_case_number

            found_user = False
            cookies = request.cookies
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

            if found_user:
                return f"Welcome back: {user}<br/>"
            else:
                remember_me = make_response('')
                remember_me.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                request.session[cookie_name] = remember_me_key
                return f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        except Exception as e:
            raise Exception("Problem executing SecureRandom.random() - TestCase") from e

        return "Weak Randomness Test executed"

class Test:

    def do_something(self, request, param):
        a36538 = param
        b36538 = a36538 + " SafeStuff"
        b36538 = b36538[:-5] + "Chars"
        map36538 = {'key36538': b36538}
        c36538 = map36538['key36538']
        d36538 = c36538[:-1]
        e36538 = d36538.encode('utf-8').decode('utf-8')
        f36538 = e36538.split(" ")[0]

        thing = ThingFactory.create_thing()
        bar = thing.do_something(f36538)

        return bar

class ThingFactory:
    @staticmethod
    def create_thing():
        return Thing()

class Thing:
    def do_something(self, input):
        return input

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
