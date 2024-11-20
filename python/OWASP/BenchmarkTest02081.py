
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-04/BenchmarkTest02081", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()
    
    param = ""
    headers = request.headers.get('BenchmarkTest02081')
    
    if headers:
        param = headers

    param = base64.urlsafe_b64decode(param).decode('utf-8')

    bar = do_something(request, param)
    
    try:
        randNumber = os.urandom(4)  # Generate a random 4-byte number
        remember_me_key = int.from_bytes(randNumber, byteorder='big') % 99

        user = "SafeInga"
        full_class_name = __name__
        test_case_number = full_class_name.split('.')[-1]  # Extract test case number
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        
        found_user = False
        cookies = request.cookies
        if cookies:
            for name, value in cookies.items():
                if cookie_name == name:
                    if value == request.cookies.get(cookie_name):
                        found_user = True

        if found_user:
            response.data = f"Welcome back: {user}<br/>".encode('utf-8')
        else:
            remember_me = make_response()
            remember_me.set_cookie(cookie_name, str(remember_me_key), secure=True, httponly=True, path=request.path)
            response.set_cookie(cookie_name, str(remember_me_key), secure=True, httponly=True)
            response.data = (
                f"{user} has been remembered with cookie: {cookie_name} whose value is: {remember_me_key}<br/>"
            ).encode('utf-8')

    except Exception as e:
        print("Problem executing SecureRandom nextInt - TestCase")
        raise e
    
    response.data += "Weak Randomness Test executed".encode('utf-8')
    return response

def do_something(request, param):
    a44156 = param
    b44156 = f"{a44156} SafeStuff"
    c44156 = b44156[:-1]

    encoded = base64.b64encode(c44156.encode())
    decoded = base64.b64decode(encoded).decode()
    
    f44156 = decoded.split(" ")[0]
   
    # Simulating the reflection here, as we don't have the ThingInterface
    bar = f"Processed: {f44156}"
    
    return bar

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
