
from flask import Flask, request, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, name):
        return self.request.args.get(name)

class ThingInterface:
    def doSomething(self, input):
        return "Processed: " + input

class ThingFactory:
    @staticmethod
    def createThing():
        return ThingInterface()

@app.route("/xss-01/BenchmarkTest00650", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00650")
    if param is None:
        param = ""

    a17321 = param
    b17321 = f"{a17321} SafeStuff"
    b17321 = b17321[:-5] + "Chars"
    map17321 = {"key17321": b17321}
    c17321 = map17321["key17321"]
    d17321 = c17321[:-1]
    e17321 = base64.b64decode(base64.b64encode(d17321.encode())).decode()
    f17321 = e17321.split(" ")[0]
    thing = ThingFactory.createThing()
    g17321 = "barbarians_at_the_gate"
    bar = thing.doSomething(g17321)

    response.headers["X-XSS-Protection"] = "0"
    response.set_data(bar)
    response.content_type = "text/html;charset=UTF-8"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
