
import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00169", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()

    param = request.headers.get("BenchmarkTest00169", "")
    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)

        bar = values_list[1]

    str_value = param if isinstance(param, str) else "No cookie value supplied"
    cookie = f'SomeCookie={str_value}; Path={request.path}; HttpOnly; Secure=False'

    response.headers.add('Set-Cookie', cookie)
    response.data = f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: false"

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
