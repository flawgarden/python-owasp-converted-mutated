
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest00736", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    values = request.values.getlist("BenchmarkTest00736")
    param = values[0] if values else ""

    num = 106
    bar = "This_should_always_happen" if (7 * 18) + num > 200 else param

    str_input = param if isinstance(param, str) else '?'
    if str_input == "":
        str_input = "No cookie value supplied"

    response.set_cookie('SomeCookie', str_input, secure=False, httponly=True, path=request.path)
    response.data = f"Created cookie: 'SomeCookie': with value: '{str_input}' and secure flag set to: false"
    response.content_type = "text/html;charset=UTF-8"
    
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
