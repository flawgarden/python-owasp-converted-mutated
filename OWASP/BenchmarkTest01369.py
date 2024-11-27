
import os
import base64
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        a43860 = param
        b43860 = a43860 + " SafeStuff"
        b43860 = b43860[:-5] + "Chars"
        map43860 = {}
        map43860["key43860"] = b43860
        c43860 = map43860["key43860"]
        d43860 = c43860[:-1]
        e43860 = base64.b64decode(base64.b64encode(d43860.encode())).decode()
        f43860 = e43860.split(" ")[0]
        return f43860

@app.route("/weakrand-03/BenchmarkTest01369", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01369", "")
    else:
        param = ""

    bar = Test().do_something(param)

    try:
        random_bytes = bytearray(40)
        random.SystemRandom().getrandbits(8 * len(random_bytes))

        remember_me_key = base64.b64encode(random_bytes).decode()

        user = "SafeBystander"
        full_class_name = "BenchmarkTest01369"
        test_case_number = full_class_name.replace("BenchmarkTest", "")
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
            resp = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
            resp.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            return resp
    except Exception as e:
        return str(e)
    finally:
        return "Randomness Test executed"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
