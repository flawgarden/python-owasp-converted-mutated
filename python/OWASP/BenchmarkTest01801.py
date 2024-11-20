
import os
import random
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    @staticmethod
    def do_something(param):
        return escape_html(param)

def escape_html(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;")
                .replace("'", "&#x27;"))

@app.route("/weakrand-04/BenchmarkTest01801", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    param = request.args.get("BenchmarkTest01801", "")

    bar = Test.do_something(param)

    try:
        rand_number = random.SystemRandom().randint(0, 98)
        remember_me_key = str(rand_number)

        user = "SafeInga"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie_name] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response += f"Welcome back: {user}<br/>"
        else:
            response += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            response += f"Set-Cookie: {cookie_name}={remember_me_key}; Secure; HttpOnly; Path={request.path}"
            request.environ['werkzeug.debug'] = remember_me_key  # Simulating setting a session attribute

    except Exception as e:
        response += f"Problem executing SecureRandom.nextInt(int) - TestCase: {str(e)}"

    response += "Weak Randomness Test executed<br/>"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
