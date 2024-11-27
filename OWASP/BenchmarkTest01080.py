
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01080", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01080", "")

    param = urllib.parse.unquote(param)

    test = Test()
    bar = test.do_something(param)

    # Simulating session storage
    request.environ['werkzeug.server.shutdown'] = bar

    return f"Item: '{encode_for_html(bar)}' with value: 10340 saved in session."

class Test:

    def do_something(self, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # Remove the 1st safe value
            bar = values_list[1]  # Get the last 'safe' value

        return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
