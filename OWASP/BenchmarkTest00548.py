
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00548", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00548":
                    param = name
                    flag = False
                    break

    a52901 = param
    b52901 = str(a52901)
    b52901 += " SafeStuff"
    b52901 = b52901[:-5] + "Chars"
    map52901 = {}
    map52901["key52901"] = b52901
    c52901 = map52901["key52901"]
    d52901 = c52901[:-1]
    e52901 = base64.b64decode(base64.b64encode(d52901.encode())).decode()
    f52901 = e52901.split(" ")[0]

    # Assuming a placeholder for ThingInterface implementation
    thing = create_thing()
    g52901 = "barbarians_at_the_gate"
    bar = thing.do_something(g52901)

    response = app.response_class(response=f"Formatted like: {bar} and b.", status=200)
    response.headers['X-XSS-Protection'] = '0'
    return response

def create_thing():
    class ThingInterface:
        def do_something(self, value):
            return f"Processed {value}"
    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
