
from flask import Flask, request, render_template, session

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'

@app.route("/trustbound-00/BenchmarkTest01145", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    names = request.headers.keys()
    for name in names:
        if name in common_headers:
            continue

        values = request.headers.getlist(name)
        if values:
            param = name
            break

    bar = Test().do_something(request, param)
    session['userid'] = bar

    return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."

class Test:
    def do_something(self, request, param):
        num = 86
        if (7 * 42) - num > 200:
            bar = "This_should_always_happen"
        else:
            bar = param

        return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

common_headers = set(['User-Agent', 'Accept', 'Host'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
