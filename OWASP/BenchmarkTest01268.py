
from flask import Flask, request, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01268", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    else:
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.form.get("BenchmarkTest01268", "")
        bar = Test().do_something(request, param)

        response.headers['X-XSS-Protection'] = "0"
        if bar:
            response.set_data(bar)
        return response

class Test:

    def do_something(self, request, param):
        a92384 = param
        b92384 = a92384 + " SafeStuff"
        b92384 = b92384[:-5] + "Chars"
        map92384 = {"key92384": b92384}
        c92384 = map92384["key92384"]
        d92384 = c92384[:-1]
        e92384 = base64.b64decode(base64.b64encode(d92384.encode())).decode()
        f92384 = e92384.split(" ")[0]
        thing = self.create_thing()
        bar = thing.do_something(f92384)

        return bar

    def create_thing(self):
        return ThingInterface()

class ThingInterface:
    def do_something(self, input):
        return input  # Placeholder

if __name__ == "__main__":
    app.run(host='0.0.0.0')
