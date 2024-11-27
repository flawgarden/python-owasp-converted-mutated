
import urllib.parse
from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01171", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response(content_type="text/html;charset=UTF-8")

    param = ""
    referer = request.headers.get("Referer")

    if referer:
        param = referer  # just grab first element

    # URL Decode the header value since request.headers.get() doesn't
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    response.headers["X-XSS-Protection"] = "0"
    obj = ["a", "b"]
    response.set_data(f"{bar} {obj}")
    return response

class Test:

    def do_something(self, param):
        bar = param
        if param and len(param) > 1:
            sbxyz83647 = list(param)
            sbxyz83647[-1] = "Z"  # replace last character with 'Z'
            bar = ''.join(sbxyz83647)

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
