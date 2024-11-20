
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-01/BenchmarkTest00747", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    response.content_type = 'text/html;charset=UTF-8'

    values = request.args.getlist("BenchmarkTest00747")
    param = values[0] if values else ""

    bar = param  # In a real scenario, we would encode this for HTML

    try:
        numGen = random.SystemRandom()

        # Get 40 random bytes
        randomBytes = bytearray(40)
        get_next_number(numGen, randomBytes)

        rememberMeKey = base64.b64encode(randomBytes).decode('utf-8')

        user = "SafeBystander"
        full_class_name = benchmark_test.__module__
        test_case_number = full_class_name.split('.')[-1].replace('BenchmarkTest', '')

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
            response.data = f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            remember_me = make_response(f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>")
            remember_me.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'] = {cookie_name: rememberMeKey}
            response = remember_me

        response.data += "Randomness Test executed".encode('utf-8')
    except Exception as e:
        print("Problem executing SecureRandom.nextBytes() - TestCase")
        raise e

    return response


def get_next_number(generator, barray):
    generator.getrandbits(len(barray) * 8)
    for i in range(len(barray)):
        barray[i] = generator.getrandbits(8)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
