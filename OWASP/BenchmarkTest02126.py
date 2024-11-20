
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02126", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest02126', '')
    bar = do_something(param)

    response = app.response_class()
    response.headers['X-XSS-Protection'] = '0'
    response.data = bar
    response.mimetype = 'text/html;charset=UTF-8'
    return response

def do_something(param):
    a64181 = param
    b64181 = a64181 + " SafeStuff"
    b64181 = b64181[:-5] + "Chars"  # replace some of the end content
    map64181 = {}
    map64181["key64181"] = b64181
    c64181 = map64181["key64181"]
    d64181 = c64181[:-1]
    e64181 = base64.b64decode(base64.b64encode(d64181.encode())).decode()
    f64181 = e64181.split(" ")[0]

    thing = create_thing()
    bar = thing.do_something(f64181)

    return bar

class ThingInterface:
    def do_something(self, input):
        return f"Result of doing something with {input}"

def create_thing():
    return ThingInterface()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
