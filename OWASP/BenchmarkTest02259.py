
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02259", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    map = request.args.to_dict()

    param = ""
    if map:
        values = map.get("BenchmarkTest02259")
        if values:
            param = values[0]

    bar = do_something(param)

    try:
        import random
        rand = random.SystemRandom().random()

        remember_me_key = str(rand)[2:]  # Trim off the 0. at the front.

        user = "SafeDonna"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1]
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        if cookies:
            for cookie in cookies:
                if cookie_name == cookie:
                    if cookies[cookie] == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data += f"Welcome back: {user}<br/>".encode()
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data += (f"{user} has been remembered with cookie: "
                              f"{cookie_name} whose value is: {remember_me_key}<br/>").encode()
            request.cookies[cookie_name] = remember_me_key

    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
        raise e

    response.data += "Weak Randomness Test random.SystemRandom().random() executed".encode()
    return response

def do_something(param):
    bar = ""
    num = 86
    if ((7 * 42) - num) > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
