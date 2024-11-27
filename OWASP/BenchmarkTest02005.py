
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02005", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = make_response()
    param = ""

    for name in request.headers:
        if name in ["User-Agent", "Accept", "Accept-Language", "Accept-Encoding", "Connection", "Host"]:
            continue  # If standard header, move on to next one

        param = name  # Grabs the name of the first non-standard header as the parameter value
        break

    bar = do_something(param)

    if param == "":
        param = "No cookie value supplied"

    response.set_cookie("SomeCookie", value=param, secure=False, httponly=True, path=request.path)

    response.data = f"Created cookie: 'SomeCookie': with value: '{param}' and secure flag set to: False"
    return response

def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-44210": "a-Value",
        "keyB-44210": param,
        "keyC": "another-Value"
    }
    bar = map_.get("keyB-44210")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
