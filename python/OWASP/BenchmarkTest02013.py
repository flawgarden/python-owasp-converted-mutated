
import os
import random
from flask import Flask, request, render_template, make_response, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = os.urandom(24)

@app.route("/weakrand-04/BenchmarkTest02013", methods=['GET', 'POST'])
def benchmark_test_02013():
    if request.method == 'GET':
        return benchmark_test_02013_post() 
    else:
        return benchmark_test_02013_post() 

def benchmark_test_02013_post():
    response = make_response()
    
    param = ""
    for name in request.headers:
        if name in common_headers:
            continue 
        param = name
        break

    bar = do_something(request, param)

    try:
        rand = random.Random().random()
        remember_me_key = str(rand)[2:]

        user = "SafeDonna"
        test_case_number = "02013"
        user += test_case_number

        cookie_name = "rememberMe" + test_case_number
        
        found_user = False
        if 'cookies' in session:
            for cookie in session['cookies']:
                if cookie_name == cookie['name']:
                    if cookie['value'] == session.get(cookie_name):
                        found_user = True
                        break

        if found_user:
            response.data = f"Welcome back: {user}<br/>"
        else:
            remember_me = {'name': cookie_name, 'value': remember_me_key}
            remember_me['secure'] = True
            remember_me['httponly'] = True
            session[cookie_name] = remember_me_key
            if 'cookies' not in session:
                session['cookies'] = []
            session['cookies'].append(remember_me)
            response.data = f"{user} has been remembered with cookie: {remember_me['name']} whose value is: {remember_me['value']}<br/>"

    except Exception as e:
        print("Problem executing SecureRandom.next() - TestCase")
        raise

    response.data += "Weak Randomness Test executed"
    return response

def do_something(request, param):
    return param # Placeholder for HTML escaping

common_headers = ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Cache-Control', 'Connection', 'DNT', 'Host', 'Keep-Alive', 'Referer', 'User-Agent', 'X-Requested-With']

if __name__ == "__main__":
    app.run(host='0.0.0.0')
