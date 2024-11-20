
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02313", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response=None,
        status=200,
        mimetype='text/html'
    )

    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest02313":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.data = f"<!DOCTYPE html>\n<html>\n<body>\n<p>Formatted like: {obj[0]} and {obj[1]}.\n</p>\n</body>\n</html>"
    return response

def do_something(param):
    a31085 = param
    b31085 = StringBuilder(a31085)
    b31085.append(" SafeStuff")
    b31085 = b31085[:-5] + "Chars"

    map31085 = {}
    map31085["key31085"] = b31085
    c31085 = map31085["key31085"]
    d31085 = c31085[:-1]

    e31085 = base64.b64decode(base64.b64encode(d31085.encode())).decode()
    f31085 = e31085.split(" ")[0]

    thing = create_thing()
    g31085 = "barbarians_at_the_gate"
    bar = thing.do_something(g31085)

    return bar

class StringBuilder:
    def __init__(self, initial):
        self.contents = [initial]

    def append(self, string):
        self.contents.append(string)

    def __str__(self):
        return ''.join(self.contents)

    def __getitem__(self, slice):
        return str(self)[slice]

    def __setitem__(self, slice, value):
        self.contents = [str(self)[:slice.start] + value + str(self)[slice.stop:]]

def create_thing():
    # Placeholder for actual implementation
    class Thing:
        def do_something(self, input):
            return f"Processed {input}"
    return Thing()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
