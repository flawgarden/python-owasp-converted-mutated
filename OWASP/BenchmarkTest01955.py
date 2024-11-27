
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01955", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response_content = "text/html;charset=UTF-8"
        param = request.headers.get("BenchmarkTest01955", "")
        param = base64.b64decode(base64.b64encode(param.encode())).decode()

        bar = do_something(param)
        request.session[bar] = "10340"

        return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
