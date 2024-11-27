
import os
from flask import Flask, request, render_template
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02510", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        values = request.form.getlist("BenchmarkTest02510")
        param = values[0] if values else ""

        bar = do_something(param)

        cmd = get_insecure_os_command_string()
        args = [cmd]
        args_env = [bar]

        try:
            result = os.popen(' '.join(args) + ' ' + ' '.join(args_env)).read()
            response.set_data(result)
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            response.set_data(escape_html(str(e)))
            return response

        return response

def do_something(param):
    a11776 = param
    b11776 = a11776 + " SafeStuff"
    b11776 = b11776[:-len("Chars")] + "Chars"
    map11776 = {"key11776": b11776}
    c11776 = map11776["key11776"]
    d11776 = c11776[:-1]
    e11776 = base64.b64decode(base64.b64encode(d11776.encode())).decode()
    f11776 = e11776.split(" ")[0]
    thing = create_thing()
    g11776 = "barbarians_at_the_gate"
    bar = thing.do_something(g11776)

    return bar

def get_insecure_os_command_string():
    # Replace with actual command retrieval logic
    return "your_command_here"

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def create_thing():
    # Placeholder for the ThingFactory.createThing() equivalent
    class ThingInterface:
        def do_something(self, input):
            return input  # Dummy implementation

    return ThingInterface()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
