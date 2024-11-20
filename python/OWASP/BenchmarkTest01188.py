
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01188", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    referer = request.headers.get("Referer")

    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    response.set_data("Parameter value: " + bar)
    return response

class Test:

    def do_something(self, param):
        bar = self.encode_for_html(param)
        return bar

    def encode_for_html(self, param):
        return escape(param)

def escape(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
