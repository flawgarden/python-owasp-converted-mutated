
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00288", methods=['GET', 'POST'])
def benchmark_test():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = ""
    if "Referer" in request.headers:
        param = request.headers["Referer"]

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map34285 = {
        "keyA-34285": "a_Value",
        "keyB-34285": param,
        "keyC": "another_Value"
    }
    bar = map34285["keyB-34285"]
    bar = map34285["keyA-34285"]

    response.headers['X-XSS-Protection'] = "0"
    length = 1
    if bar is not None:
        length = len(bar)
        response.set_data(bar[:length])

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
