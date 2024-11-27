
import os
import base64
from flask import Flask, request, render_template, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest00087", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("securecookie-00/BenchmarkTest00087.html"))
        user_cookie = ("BenchmarkTest00087", "whatever", 60 * 3)  # Store cookie for 3 minutes
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=True, path=request.path, domain=request.host)
        return response
    
    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if 'BenchmarkTest00087' in the_cookies:
            param = the_cookies['BenchmarkTest00087']
        
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        
        input_param = param
        str_param = ""
        if isinstance(input_param, str):
            str_param = input_param
        if str_param == "":
            str_param = "No cookie value supplied"
        
        cookie = ("SomeCookie", str_param)
        response = make_response(f"Created cookie: 'SomeCookie': with value: '{str_param}' and secure flag set to: false")
        response.set_cookie(cookie[0], cookie[1], secure=False, httponly=True, path=request.path)
        return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
