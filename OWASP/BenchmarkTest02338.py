
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-05/BenchmarkTest02338", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02338":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    import random
    remember_me_key = str(random.randint(0, 2**63 - 1))

    user = "Logan"
    full_class_name = benchmark_test.__class__.__name__
    test_case_number = full_class_name[full_class_name.rfind('.') + 1 + len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for key, value in cookies.items():
            if cookie_name == key:
                if value == request.cookies.get(cookie_name):
                    found_user = True
                    break

    response = make_response()
    if found_user:
        response.set_data(f"Welcome back: {user}<br/>")
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
        response.set_data(f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>")

    response.set_data(response.get_data(as_text=True) + "Weak Randomness Test executed")
    return response

def do_something(param):
    num = 106
    return "This_should_always_happen" if (7 * 18) + num > 200 else param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
