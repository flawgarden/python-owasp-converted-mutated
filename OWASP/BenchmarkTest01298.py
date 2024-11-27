
from flask import Flask, request, render_template, make_response
import random
import html

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01298", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = request.args.get("BenchmarkTest01298", "")
    bar = Test().do_something(param)

    try:
        r = random.SystemRandom().randint(0, 2147483647)
        remember_me_key = str(r)

        user = "SafeIngrid"
        full_class_name = benchmark_test.__module__ + "." + benchmark_test.__qualname__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response(user + f" has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.cookies[cookie_name] = remember_me_key

        response.data += "Weak Randomness Test random.SystemRandom().randint() executed"
    except Exception as e:
        print("Problem executing random.SystemRandom().randint() - TestCase")
        raise

    return response

class Test:

    def do_something(self, param):
        bar = html.escape(param)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
