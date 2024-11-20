
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00243", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Referer', 'Cookie']:
            continue

        values = request.headers.getlist(name)
        if values:
            param = name
            break

    bar = "safe!"
    map86025 = {
        "keyA-86025": "a-Value",
        "keyB-86025": param,
        "keyC": "another-Value"
    }
    bar = map86025["keyB-86025"]

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeBystander"
        test_case_number = "00243"
        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        return str(e)

    response.data += "Randomness Test os.urandom executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
