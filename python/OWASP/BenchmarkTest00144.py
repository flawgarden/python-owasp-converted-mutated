
import urllib.parse
from flask import Flask, request, make_response, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00144", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = make_response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = ""
        if request.headers.get("Referer"):
            param = request.headers.get("Referer")

        param = urllib.parse.unquote(param)

        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value

        response.headers['X-XSS-Protection'] = '0'
        obj = ["a", "b"]
        response.data = f"{bar} {obj}"
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
