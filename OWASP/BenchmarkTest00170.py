
import os
import base64
from flask import Flask, request, render_template, make_response
from werkzeug.utils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/securecookie-00/BenchmarkTest00170", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get("BenchmarkTest00170", "")
    param = escape(param)  # URL Decode the header value

    # Chain a bunch of propagators in sequence
    a9823 = param  # assign
    b9823 = a9823 + " SafeStuff"  # append some safe content

    # Replace some of the end content
    b9823 = b9823[:-len("Chars")] + "Chars"

    map9823 = {}
    map9823["key9823"] = b9823  # put in a collection
    c9823 = map9823["key9823"]  # get it back out
    d9823 = c9823[:-1]  # extract most of it
    e9823 = base64.b64decode(base64.b64encode(d9823.encode())).decode()  # B64 encode and decode it
    f9823 = e9823.split(" ")[0]  # split it on a space

    # Simulating the ThingInterface and creating a 'thing'
    class ThingInterface:
        def doSomething(self, input):
            return "Received: " + input

    thing = ThingInterface()
    g9823 = "barbarians_at_the_gate"  # This is static so this whole flow is 'safe'
    bar = thing.doSomething(g9823)  # reflection

    str_cookie_value = param if param else "No cookie value supplied"
    response = make_response("Created cookie: 'SomeCookie': with value: '{}'".format(escape(str_cookie_value)))

    cookie = "SomeCookie={}; Path={}; HttpOnly;".format(str_cookie_value, request.path)
    response.headers.add('Set-Cookie', cookie)

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
