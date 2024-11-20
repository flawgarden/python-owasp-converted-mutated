
import os
import base64
from flask import Flask, request, render_template, make_response, session, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)


@app.route("/weakrand-04/BenchmarkTest01931", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = make_response()
    
    param = ""
    if request.headers.get("BenchmarkTest01931"):
        param = request.headers.get("BenchmarkTest01931")
    
    param = param.replace("%20", " ")  # URL decode

    bar = do_something(param)

    rand = os.urandom(4).hex()  # Generate random string
    remember_me_key = rand[2:]  # Trim off the 0. at the front.

    user = "Floyd"
    full_class_name = "BenchmarkTest01931"
    test_case_number = full_class_name.split("BenchmarkTest")[-1]
    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    found_user = False
    cookies = request.cookies
    if cookies:
        for cookie in cookies:
            if cookie_name == cookie:
                if cookies[cookie_name] == session.get(cookie_name):
                    found_user = True

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, domain=request.host)
        session[cookie_name] = remember_me_key
        response.data = f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"

    response.data += "Weak Randomness Test executed"
    return response


def do_something(param):
    a40465 = param
    b40465 = f"{a40465} SafeStuff"
    b40465 = b40465[:-5] + "Chars"  # Replace "Stuff" with "Chars"
    map40465 = {"key40465": b40465}
    c40465 = map40465["key40465"]
    d40465 = c40465[:-1]
    e40465 = base64.b64decode(base64.b64encode(d40465.encode())).decode()  # B64 encode and decode
    f40465 = e40465.split(" ")[0]
    
    # Simulate reflection - adapt as necessary for your own implementation
    # Here you would call your actual method instead
    bar = f"Reflected value: {f40465}"  
    
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
