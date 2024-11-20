
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00079", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        resp = make_response(render_template("weakrand-00/BenchmarkTest00079.html"))
        resp.set_cookie("BenchmarkTest00079", "whatever", max_age=60 * 3, secure=True, path=request.path, domain=request.host.split(':')[0])
        return resp

    elif request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"

        if "BenchmarkTest00079" in cookies:
            param = cookies["BenchmarkTest00079"]
        
        bar = "safe!"
        map18384 = {
            "keyA-18384": "a-Value",
            "keyB-18384": param,
            "keyC": "another-Value"
        }
        bar = map18384["keyB-18384"]

        rand = random.random()
        rememberMeKey = str(rand).split('.')[1]

        user = "Floyd"
        full_class_name = benchmark_test.__module__ + '.' + benchmark_test.__name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        found_user = False

        if 'rememberMe' + test_case_number in cookies:
            if cookies[cookie_name] == request.environ.get('werkzeug.session').get(cookie_name):
                found_user = True

        if found_user:
            return f"Welcome back: {user}<br/>"
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, path=request.path, domain=request.host.split(':')[0])
            request.environ.get('werkzeug.session')[cookie_name] = rememberMeKey
            return f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>"

    return "Weak Randomness Test executed"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
