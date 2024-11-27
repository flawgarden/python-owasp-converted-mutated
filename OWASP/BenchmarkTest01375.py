
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/trustbound-00/BenchmarkTest01375", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.values.get('BenchmarkTest01375', '')

    bar = Test().do_something(request, param)

    # Simulating session storage in Flask
    with app.app_context():
        from flask import session
        session['userid'] = bar

    return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."

class Test:

    def do_something(self, request, param):
        a33070 = param
        b33070 = a33070 + " SafeStuff"
        b33070 = b33070[:-5] + "Chars"
        map33070 = {"key33070": b33070}
        c33070 = map33070["key33070"]
        d33070 = c33070[:-1]
        e33070 = base64.b64decode(base64.b64encode(d33070.encode())).decode()
        f33070 = e33070.split(" ")[0]
        thing = ThingFactory.create_thing()
        bar = thing.do_something(f33070)

        return bar

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("'", "&#39;").replace('"', "&quot;")

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

class ThingInterface:
    def do_something(self, input_str):
        return input_str[::-1]  # Example transformation

if __name__ == "__main__":
    app.run(host='0.0.0.0')
