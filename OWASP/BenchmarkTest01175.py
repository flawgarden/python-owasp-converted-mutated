
from flask import Flask, request, Response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01175", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    param = ""
    referer_header = request.headers.get('Referer')

    if referer_header:
        param = referer_header

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = f"Formatted like: a and {bar}."
    response.content_type = "text/html;charset=UTF-8"
    return response

class Test:
    def do_something(self, param):
        bar = self.encode_for_html(param)
        return bar

    def encode_for_html(self, param):
        # Simple HTML encoding implementation
        return param.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
