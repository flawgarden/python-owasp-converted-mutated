
from flask import Flask, request, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest02064", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    headers = request.headers.getlist("BenchmarkTest02064")

    if headers:
        param = headers[0]  # Just grab first element

    param = urllib.parse.unquote(param)  # URL Decode the header value
    bar = do_something(param)

    if not param:
        param = "No cookie value supplied"

    response = make_response("Created cookie: 'SomeCookie': with value: '" + str(param) + "' and secure flag set to: true")
    response.set_cookie("SomeCookie", param, secure=True, httponly=True, path=request.path)

    return response

def do_something(param):
    bar = "safe!"
    map96496 = {
        "keyA-96496": "a_Value",  # put some stuff in the collection
        "keyB-96496": param,  # put it in a collection
        "keyC": "another_Value"  # put some stuff in the collection
    }
    bar = map96496["keyB-96496"]  # get it back out
    bar = map96496["keyA-96496"]  # get safe value back out

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
