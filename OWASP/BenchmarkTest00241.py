
import os
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00241", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    for name in request.headers:
        if name in ['User-Agent', 'Accept', 'Content-Type', 'Host']:  # Common headers
            continue
        param = name
        break

    bar = "This_should_always_happen" if ((7 * 42) - 86 > 200) else param

    input_data = b""
    str_value = "?"

    if isinstance(param, str):
        str_value = param
    elif isinstance(param, bytes):
        input_data = request.data
        if not input_data:
            return "This input source requires a POST, not a GET. Incompatible UI for the InputStream source."
        str_value = input_data.decode()

    if str_value == "":
        str_value = "No cookie value supplied"

    response.set_cookie("SomeCookie", str_value, secure=False, httponly=True, path=request.path)

    return f"Created cookie: 'SomeCookie': with value: '{str_value}' and secure flag set to: false"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
