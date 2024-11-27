
from flask import Flask, request, session, render_template
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'your_secret_key'

@app.route("/trustbound-01/BenchmarkTest02016", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    for name in request.headers:
        if name in common_headers():
            continue

        param = name
        break

    bar = do_something(param)

    session['userid'] = bar

    return "Item: 'userid' with value: '{}' saved in session.".format(encode_for_html(bar))

def do_something(param):
    thing = create_thing()
    bar = thing.do_something(param)
    return bar

def common_headers():
    return ['Content-Type', 'User-Agent', 'Accept', 'Host']

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    # Placeholder for actual implementation
    class ThingInterface:
        def do_something(self, param):
            return param[::-1]  # Just an example of processing the input

    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
