
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-01/BenchmarkTest00883", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response_value = 'text/html;charset=UTF-8'
    param = request.args.get("BenchmarkTest00883")

    a69063 = param  # assign
    b69063 = a69063 + " SafeStuff"  # stick in string builder
    b69063 = b69063[:-5] + "Chars"  # replace some of the end content
    map69063 = {} 
    map69063["key69063"] = b69063  # put in a collection
    c69063 = map69063["key69063"]  # get it back out
    d69063 = c69063[:-1]  # extract most of it
    e69063 = base64.b64decode(base64.b64encode(d69063.encode())).decode()  # B64 encode and decode it
    f69063 = e69063.split(" ")[0]  # split it on a space
    thing = create_thing()  # reflection
    bar = thing.do_something(f69063)  # reflection

    return f"Formatted like: a and {bar}.", response_value

def create_thing():
    class ThingInterface:
        def do_something(self, value):
            return f"Processed {value}"

    return ThingInterface()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
