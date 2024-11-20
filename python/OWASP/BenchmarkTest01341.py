
import base64
from flask import Flask, request, Response, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01341", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers["Content-Type"] = "text/html;charset=UTF-8"

    param = request.args.get('BenchmarkTest01341', '')

    bar = Test().do_something(request, param)

    response.headers["X-XSS-Protection"] = "0"
    response.data = "Formatted like: {} and {}.".format("a", bar)
    return response

class Test:

    def do_something(self, request, param):
        a41908 = param
        b41908 = str(a41908) + " SafeStuff"
        b41908 = b41908[:-5] + "Chars"  # replace end content
        map41908 = {}
        map41908['key41908'] = b41908
        c41908 = map41908['key41908']
        d41908 = c41908[:-1]  # extract most of it
        e41908 = base64.b64decode(base64.b64encode(d41908.encode())).decode()  # B64 encode and decode

        f41908 = e41908.split(" ")[0]  # split it on a space
        thing = ThingFactory.create_thing()
        g41908 = "barbarians_at_the_gate"
        bar = thing.do_something(g41908)

        return bar

class ThingInterface:
    def do_something(self, g):
        # Implementation of the method
        return g

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
