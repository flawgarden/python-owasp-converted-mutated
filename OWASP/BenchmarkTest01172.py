
import urllib.parse
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01172", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = "text/html;charset=UTF-8"

        param = ""
        headers = request.headers.get('Referer')

        if headers:
            param = headers  # grab first element

        # URL Decode the header value
        param = urllib.parse.unquote(param)

        bar = Test().do_something(request, param)

        response.headers['X-XSS-Protection'] = "0"
        obj = ("a", bar)
        response.set_data("Formatted like: %s and %s." % obj)
        return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map35084 = {
            "keyA-35084": "a-Value",
            "keyB-35084": param,
            "keyC": "another-Value"
        }
        bar = map35084["keyB-35084"]  # get it back out

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
