
from flask import Flask, request, render_template
import os
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest01744", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    param = request.values.get("BenchmarkTest01744", "")

    bar = Test().do_something(request, param)

    file_target = os.path.join('testfiles', bar)
    response += f"Access to file: '{html_encode(file_target)}' created.\n"
    if os.path.exists(file_target):
        response += " And file already exists."
    else:
        response += " But file doesn't exist yet."

    return response

class Test:

    def do_something(self, request, param):
        a17402 = param
        b17402 = str(a17402) + " SafeStuff"
        b17402 = b17402[:-5] + "Chars"

        map17402 = { "key17402": b17402 }
        c17402 = map17402["key17402"]
        d17402 = c17402[:-1]
        e17402 = base64.b64decode(base64.b64encode(d17402.encode())).decode()

        f17402 = e17402.split(" ")[0]
        g17402 = "barbarians_at_the_gate"
        bar = self.create_thing().do_something(g17402)

        return bar

    def create_thing(self):
        return ThingInterface()

class ThingInterface:
    def do_something(self, g):
        return g

def html_encode(s):
    return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
