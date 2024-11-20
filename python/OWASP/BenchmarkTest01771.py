
from flask import Flask, request, make_response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-03/BenchmarkTest01771", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.args.get("BenchmarkTest01771")
    bar = Test().do_something(param)

    response = make_response(bar)
    response.headers["X-XSS-Protection"] = "0"
    return response


class Test:

    def do_something(self, param):
        a58724 = param
        b58724 = str(a58724) + " SafeStuff"
        b58724 = b58724[:-5] + "Chars"
        
        map58724 = {'key58724': b58724}
        c58724 = map58724['key58724']
        d58724 = c58724[:-1]
        e58724 = base64.b64decode(base64.b64encode(d58724.encode())).decode()
        f58724 = e58724.split(" ")[0]

        thing = self.create_thing()
        bar = thing.do_something(f58724)

        return bar

    def create_thing(self):
        return ThingInterface()


class ThingInterface:
    def do_something(self, value):
        return f"Processed value: {value}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
