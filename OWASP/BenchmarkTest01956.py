
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-01/BenchmarkTest01956", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""

    param = request.headers.get("BenchmarkTest01956", "")
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    # Simulating the behavior of HttpSession.putValue
    request.environ['session'][bar] = "10340"

    response += f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."
    return response

def do_something(request, param):
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

def encode_for_html(str_value):
    return str_value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
