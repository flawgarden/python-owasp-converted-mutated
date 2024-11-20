
import os
import random
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-03/BenchmarkTest01368", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.args.get("BenchmarkTest01368", "")

    bar = Test().do_something(param)

    try:
        random_bytes = os.urandom(40)
        remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

        user = "SafeByron"
        full_class_name = "BenchmarkTest01368"  # Placeholder for class name
        test_case_number = full_class_name.replace("BenchmarkTest", "")
        user += test_case_number

        cookie_name = f"rememberMe{test_case_number}"

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.set_data(f"Welcome back: {user}<br/>")
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            request.environ['werkzeug.session'] = remember_me_key
            response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    except Exception as e:
        print("Problem executing SecureRandom.urandom() - TestCase")
        raise

    response.set_data(response.get_data(as_text=True) + "Randomness Test executed")
    return response


class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = param.split(" ")[0]
        return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
