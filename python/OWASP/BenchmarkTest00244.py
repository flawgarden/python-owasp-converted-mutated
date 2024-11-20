
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-00/BenchmarkTest00244", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = make_response()
    
    param = ''
    headers = request.headers
    for name in headers:
        if name not in ['Content-Type', 'User-Agent', 'Accept', 'Accept-Encoding', 'Accept-Language', 'Connection']:
            param = name
            break

    bar = param if (500 / 42) + 196 > 200 else "This should never happen"

    try:
        random_bytes = random.SystemRandom().getrandbits(40 * 8).to_bytes(40, 'big')
        remember_me_key = random_bytes.hex()

        user = "SafeBystander"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name in cookies:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'].get('session')['rememberMe' + test_case_number] = remember_me_key
            response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise

    response.data += "Randomness Test executed"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
