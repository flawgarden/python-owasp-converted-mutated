
import base64
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01254", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01254", "")
    bar = Test().do_something(param)

    response = make_response(bar)
    response.headers["X-XSS-Protection"] = "0"
    return response

class Test:

    def do_something(self, param):
        a23874 = param
        b23874 = a23874 + " SafeStuff"
        b23874 = b23874[:-5] + "Chars"

        map23874 = {}
        map23874["key23874"] = b23874
        c23874 = map23874["key23874"]
        d23874 = c23874[:-1]
        e23874 = base64.b64decode(base64.b64encode(d23874.encode())).decode()
        f23874 = e23874.split(" ")[0]

        thing = create_thing()
        bar = thing.do_something(f23874)

        return bar

def create_thing():
    # Placeholder for actual implementation
    class ThingInterface:
        def do_something(self, value):
            return f"Processed {value}"

    return ThingInterface()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
