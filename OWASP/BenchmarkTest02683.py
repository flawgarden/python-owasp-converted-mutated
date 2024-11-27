
from flask import Flask, request, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02683", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest02683")
    bar = do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

def do_something(param):
    a47309 = param
    b47309 = str(a47309) + " SafeStuff"
    b47309 = b47309[:-5] + "Chars"
    map47309 = {"key47309": b47309}
    c47309 = map47309["key47309"]
    d47309 = c47309[:-1]
    e47309 = base64.b64decode(base64.b64encode(d47309.encode())).decode()
    f47309 = e47309.split(" ")[0]
    thing = create_thing()
    g47309 = "barbarians_at_the_gate"
    bar = thing.do_something(g47309)

    return bar

def create_thing():
    class Thing:
        def do_something(self, input):
            return f"Proceeded with {input}"

    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
