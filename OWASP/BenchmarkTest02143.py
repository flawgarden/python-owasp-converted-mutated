
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/securecookie-00/BenchmarkTest02143", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = request.form.get("BenchmarkTest02143", "")
    bar = do_something(param)

    if not param:
        param = "No cookie value supplied"
    cookie = f"SomeCookie={param}; Secure; HttpOnly; Path={request.path}"
    response.set_cookie("SomeCookie", param, secure=True, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{bar}' and secure flag set to: true"
    return response


def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-44285": "a_Value",
        "keyB-44285": param,
        "keyC": "another_Value"
    }
    bar = map_.get("keyB-44285")
    bar = map_.get("keyA-44285")
    return bar


if __name__ == "__main__":
    app.run(host='0.0.0.0')
