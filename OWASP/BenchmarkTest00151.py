
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00151", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("Referer"):
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)

        bar = values_list[1]

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.response = f"{bar}" % obj
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
