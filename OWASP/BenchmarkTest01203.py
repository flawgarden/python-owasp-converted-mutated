
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01203", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    param = ""

    headers = request.headers.get('BenchmarkTest01203')

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    # Simulated session storage
    request.session = {}
    request.session['userid'] = bar

    return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."

class Test:
    def do_something(self, param):
        bar = "safe!"
        map72700 = {}
        map72700["keyA-72700"] = "a-Value"
        map72700["keyB-72700"] = param
        map72700["keyC"] = "another-Value"
        bar = map72700["keyB-72700"]
        return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
