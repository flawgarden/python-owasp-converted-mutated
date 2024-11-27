
from flask import Flask, request, render_template, jsonify
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02363", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02363":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(request, param)

    try:
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        # DatabaseHelper.JDBCtemplate.batchUpdate(sql)
        return f"No results can be displayed for query: {html_escape(sql)}<br> because the Spring batchUpdate method doesn't return results."
    except Exception as e:
        return "Error processing request."

def do_something(request, param):
    a21456 = param
    b21456 = a21456 + " SafeStuff"
    b21456 = b21456[:-5] + "Chars"
    map21456 = {'key21456': b21456}
    c21456 = map21456['key21456']
    d21456 = c21456[:-1]
    e21456 = base64.b64decode(base64.b64encode(d21456.encode())).decode()
    f21456 = e21456.split(" ")[0]
    thing = ThingFactory.create_thing()
    g21456 = "barbarians_at_the_gate"
    bar = thing.do_something(g21456)

    return bar

def html_escape(text):
    """Escapes HTML characters in a string to prevent XSS."""
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")

class ThingInterface:
    def do_something(self, input):
        return "static_output"

class ThingFactory:
    @staticmethod
    def create_thing():
        return ThingInterface()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
