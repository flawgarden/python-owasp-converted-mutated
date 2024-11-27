
import os
from flask import Flask, request, render_template, make_response
import random
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-03/BenchmarkTest01447", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = make_response()
        response.headers["Content-Type"] = "text/html;charset=UTF-8"

        param = ""
        found = False
        names = request.args.keys()
        for name in names:
            values = request.args.getlist(name)
            for value in values:
                if value == "BenchmarkTest01447":
                    param = name
                    found = True
                    break
            if found:
                break

        bar = Test().do_something(request, param)

        try:
            random_bytes = bytearray(40)
            random.seed(0)  # Seed for reproducibility
            for i in range(40):
                random_bytes[i] = random.getrandbits(8)

            remember_me_key = base64.b64encode(random_bytes).decode('utf-8')

            user = "SafeBystander"
            test_case_number = "01447"  # Extracted from class naming convention
            user += test_case_number

            cookie_name = f"rememberMe{test_case_number}"

            found_user = False
            cookies = request.cookies
            if cookie_name in cookies:
                if cookies[cookie_name] == request.cookies.get(cookie_name):
                    found_user = True

            if found_user:
                response.data = f"Welcome back: {user}<br/>".encode()
            else:
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>".encode()

        except Exception as e:
            print("Problem executing SecureRandom.nextBytes() - TestCase")
            raise e
        finally:
            response.data += b"Randomness Test executed<br/>"

        return response

class Test:

    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
