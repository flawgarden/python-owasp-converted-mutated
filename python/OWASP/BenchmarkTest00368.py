
from flask import Flask, request, render_template
import random
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/weakrand-00/BenchmarkTest00368", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = request.form.get('BenchmarkTest00368', "")
    bar = urllib.parse.quote(param, safe='')

    value = random.random()
    rememberMeKey = str(value)[2:]

    user = "Doug"
    full_class_name = "BenchmarkTest00368"
    test_case_number = full_class_name[len("BenchmarkTest"):]

    user += test_case_number

    cookie_name = "rememberMe" + test_case_number

    cookies = request.cookies
    found_user = cookie_name in cookies and cookies[cookie_name] == request.cookies.get(cookie_name)

    if found_user:
        response.data = f"Welcome back: {user}<br/>"
    else:
        response.set_cookie(cookie_name, rememberMeKey, secure=True, httponly=True)
        request.environ['werkzeug.session'].set(cookie_name, rememberMeKey)
        response.data = (
            f"{user} has been remembered with cookie: {cookie_name} whose value is: {rememberMeKey}<br/>"
        )

    response.data += "Weak Randomness Test random.random() executed"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
