
import os
import base64
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:
    @staticmethod
    def do_something(param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

@app.route("/weakrand-02/BenchmarkTest01294", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    response.content_type = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest01294", "")
    bar = Test.do_something(param)

    try:
        rand = os.urandom(4)  # Use os.urandom for cryptographically secure random numbers
        remember_me_key = str(int.from_bytes(rand, 'big'))  # Convert to an integer for the key

        user = "SafeFloyd"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1].replace("BenchmarkTest", "")

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies

        if cookies:
            for cookie_key in cookies:
                if cookie_name == cookie_key:
                    if cookies[cookie_key] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = (cookie_name, remember_me_key)
            response.set_cookie(remember_me[0], remember_me[1], secure=True, httponly=True, path=request.full_path)
            response.data = f"{user} has been remembered with cookie: {remember_me[0]} whose value is: {remember_me[1]}<br/>"
        
    except Exception as e:
        print("Problem executing random number generation - TestCase")
        raise e

    response.data += "Weak Randomness Test os.urandom executed"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
