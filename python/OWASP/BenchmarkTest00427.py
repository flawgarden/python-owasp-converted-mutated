
from flask import Flask, request, render_template, session
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.secret_key = 'supersecretkey'

@app.route("/trustbound-00/BenchmarkTest00427", methods=['GET', 'POST'])
def benchmark_test00427():
    if request.method == 'GET':
        return benchmark_test00427_post()
    return benchmark_test00427_post()

def benchmark_test00427_post():
    param = request.args.get("BenchmarkTest00427", "")
    
    a70670 = param
    b70670 = a70670 + " SafeStuff"
    b70670 = b70670[:-5] + "Chars"
    
    map70670 = {}
    map70670["key70670"] = b70670
    c70670 = map70670["key70670"]
    d70670 = c70670[:-1]
    e70670 = base64.b64decode(base64.b64encode(d70670.encode())).decode()
    f70670 = e70670.split(" ")[0]
    
    thing = create_thing()
    bar = thing.do_something(f70670)
    
    session['userid'] = bar
    
    return f"Item: 'userid' with value: '{encode_for_html(bar)}' saved in session."

def create_thing():
    # Placeholder for the actual 'ThingInterface' implementation
    class Thing:
        def do_something(self, value):
            return "Processed " + value
    
    return Thing()

def encode_for_html(value):
    return value.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
