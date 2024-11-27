
from flask import Flask, request, session, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'supersecretkey'  # Required for session management

@app.route("/trustbound-00/BenchmarkTest01550", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = request.form.get("BenchmarkTest01550", "")
        bar = Test().do_something(request, param)
        session['userid'] = bar
        return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."

class Test:

    def do_something(self, request, param):
        a86153 = param  # assign
        b86153 = a86153 + " SafeStuff"  # append some safe content
        b86153 = b86153[:-5] + "Chars"  # replace some of the end content
        map86153 = {'key86153': b86153}  # put in a collection
        c86153 = map86153['key86153']  # get it back out
        d86153 = c86153[:-1]  # extract most of it
        e86153 = base64.b64decode(base64.b64encode(d86153.encode())).decode()  # B64 encode and decode it
        f86153 = e86153.split(" ")[0]  # split it on a space
        thing = ThingFactory.create_thing()
        bar = thing.do_something(f86153)  # reflection
        return bar

def encode_for_html(value):
    return value.replace("<", "&lt;").replace(">", "&gt;")

class ThingInterface:
    def do_something(self, value):
        return value  # Placeholder for the actual implementation

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
