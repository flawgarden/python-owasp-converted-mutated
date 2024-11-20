
import os
from flask import Flask, request, render_template, make_response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest00404", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = make_response()
    param = request.args.get('BenchmarkTest00404', '')

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    input_param = param
    str_value = param if isinstance(input_param, str) else ""
    
    if str_value == "":
        str_value = "No cookie value supplied"
        
    cookie = f'SomeCookie={str_value}; Secure; HttpOnly; Path=/securecookie-00/BenchmarkTest00404'
    response.headers.add('Set-Cookie', cookie)

    response.data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: true"
    return response


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
