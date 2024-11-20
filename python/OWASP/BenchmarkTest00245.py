
import os
import random
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00245", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    param = ""
    
    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Accept-Language', 'Content-Type']:
            continue
        param = name
        break

    a73565 = param
    b73565 = str(a73565) + " SafeStuff"
    b73565 = b73565[:-5] + "Chars"
    
    map73565 = {}
    map73565["key73565"] = b73565
    c73565 = map73565["key73565"]
    d73565 = c73565[:-1]
    
    # Dummy encoding as Python's Base64 decoding/encoding is not the same as Java's
    e73565 = d73565.encode('utf-8').decode('utf-8') 

    f73565 = e73565.split(" ")[0]
    
    # Simulate the behavior of a ThingInterface
    g73565 = "barbarians_at_the_gate"
    bar = g73565  # Placeholder for actual reflection

    try:
        rand = random.random()
        remember_me_key = str(rand)[2:]
        
        user = "SafeDonatella"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1][len("BenchmarkTest"):]

        user += test_case_number
        cookie_name = "rememberMe" + test_case_number

        found_user = False
        cookies = request.cookies
        
        if cookie_name in cookies:
            if cookies[cookie_name] == request.cookies.get(cookie_name):
                found_user = True

        if found_user:
            response.data += f"Welcome back: {user}<br/>"
        else:
            response.set_cookie(cookie_name, remember_me_key, secure=True, httponly=True, path=request.path)
            response.data += f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
        
    except Exception as e:
        print("Problem executing SecureRandom.nextDouble() - TestCase")
    
    response.data += "Weak Randomness Test random.random() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
