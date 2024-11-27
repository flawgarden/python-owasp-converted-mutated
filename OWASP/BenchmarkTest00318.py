
import os
import base64
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00318", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    
    param = request.headers.get('BenchmarkTest00318', '')
    param = base64.b64decode(param.encode()).decode('utf-8', errors='ignore')

    a30925 = param
    b30925 = f"{a30925} SafeStuff"
    c30925 = b30925[:-1]  # extract most of it
    e30925 = base64.b64decode(base64.b64encode(c30925.encode())).decode()  # B64 encode and decode
    f30925 = e30925.split(" ")[0]

    thing = "ThingObjectPlaceholder"  # Placeholder for actual ThingInterface object
    g30925 = "barbarians_at_the_gate"
    bar = f"ReflectionResult: {g30925}"  # Placeholder for the reflection call

    try:
        rand = random.random()
        remember_me_key = str(rand)[2:]

        user = "SafeFloyd"
        test_case_number = "00318"
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

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
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextFloat() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
