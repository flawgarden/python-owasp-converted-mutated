
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01257", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.args.get("BenchmarkTest01257", "")
    bar = Test().do_something(param)

    response.headers['X-XSS-Protection'] = "0"
    response.set_data(bar)
    return response

class Test:

    def do_something(self, param):
        thing = self.create_thing()
        bar = thing.do_something(param)
        return bar

    def create_thing(self):
        # Simulate the creation of a ThingInterface
        class ThingInterface:
            def do_something(self, input_param):
                return f"Processed: {input_param}"
        return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
