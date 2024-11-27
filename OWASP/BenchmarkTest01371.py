
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/weakrand-03/BenchmarkTest01371", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = make_response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.args.get('BenchmarkTest01371', '')

        bar = Test().do_something(request, param)

        try:
            r = random.SystemRandom().randint(0, 2**31 - 1)
            remember_me_key = str(r)

            user = "SafeIngrid"
            full_class_name = benchmark_test.__module__
            test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

            user += test_case_number
            cookie_name = "rememberMe" + test_case_number

            found_user = False
            cookies = request.cookies
            if cookies:
                for cookie in cookies:
                    if cookie_name == cookie:
                        if cookies[cookie].encode() == request.cookies.get(cookie_name).encode():
                            found_user = True

            if found_user:
                response.set_data(f"Welcome back: {user}<br/>")
            else:
                response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
                request.environ['werkzeug.session'].set(cookie_name, remember_me_key)
                response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")
        except Exception as e:
            print("Problem executing SecureRandom.randint() - TestCase")
            raise e

        response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
        return response
    return render_template("index.html")


class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        
        return bar


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
