
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00147", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.content_type = "text/html;charset=UTF-8"

    param = ""
    if request.headers.get("Referer") is not None:
        param = request.headers.get("Referer")

    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = ["safe", param, "moresafe"]

        values_list.pop(0)  # remove the 1st safe value

        bar = values_list[1]  # get the last 'safe' value

    response.headers["X-XSS-Protection"] = "0"
    response.data = "Formatted like: {} and {}.".format("a", bar)
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
