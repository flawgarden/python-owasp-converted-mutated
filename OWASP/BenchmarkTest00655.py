
import os
from flask import Flask, request, render_template, make_response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00655", methods=['GET', 'POST'])
def benchmark_test00655():
    if request.method == 'GET':
        return benchmark_test00655_post()
    return benchmark_test00655_post()

def benchmark_test00655_post():
    response = make_response()
    param = request.args.get("BenchmarkTest00655", "")

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    str_value = "?"
    input_param = param
    if isinstance(input_param, str):
        str_value = input_param

    if str_value == "":
        str_value = "No cookie value supplied"

    response.set_cookie('SomeCookie', str_value, secure=True, httponly=True, path=request.path)
    
    response_data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: true"
    response.data = response_data
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
