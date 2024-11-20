
import base64
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01515", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.args.get("BenchmarkTest01515", default="", type=str)

    result = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    response.data = result
    return response

class Test:
    def do_something(self, request, param):
        a84124 = param
        b84124 = str(a84124)
        b84124 += " SafeStuff"
        b84124 = b84124[:-len("Chars")] + "Chars"
        
        map84124 = {}
        map84124["key84124"] = b84124
        c84124 = map84124["key84124"]
        d84124 = c84124[:-1]
        e84124 = base64.b64decode(base64.b64encode(d84124.encode())).decode()
        f84124 = e84124.split(" ")[0]
        
        thing = ThingFactory.create_thing()
        g84124 = "barbarians_at_the_gate"
        bar = thing.do_something(g84124)

        return bar

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

class ThingInterface:
    def do_something(self, input_string):
        # Simulate reflection-like behavior
        return f"Processed: {input_string}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
