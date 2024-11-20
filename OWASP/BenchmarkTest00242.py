
from flask import Flask, request, make_response
import werkzeug

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00242", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = make_response()

    param = ""
    for name in request.headers:
        if name in common_headers():
            continue

        param = name
        break

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[0]

    str_value = param if param else "No cookie value supplied"
    cookie = werkzeug.datastructures.Cookie('SomeCookie', str_value)

    cookie.set_secure(True)
    cookie.set_http_only(True)
    cookie.set_path(request.path)
    response.set_cookie(cookie.name, cookie.value, secure=cookie.secure, httponly=cookie.http_only, path=cookie.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: true"
    return response

def common_headers():
    return ['Accept', 'Accept-Charset', 'Accept-Encoding', 'Accept-Language', 'Connection', 'Host', 'User-Agent']

if __name__ == "__main__":
    app.run(host='0.0.0.0')
