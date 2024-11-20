
import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True
TESTFILES_DIR = "uploads/"  # or your designated path

class SeparateClassRequest:
    def __init__(self, request):
        self.request = request

    def getTheParameter(self, param_name):
        return self.request.args.get(param_name)

class ThingInterface:
    def doSomething(self, value):
        return value  # replace with your actual logic

class ThingFactory:
    @staticmethod
    def createThing():
        return ThingInterface()

@app.route("/pathtraver-00/BenchmarkTest00628", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = ""
    scr = SeparateClassRequest(request)
    param = scr.getTheParameter("BenchmarkTest00628")
    if param is None:
        param = ""

    a24315 = param
    b24315 = a24315 + " SafeStuff"
    b24315 = b24315[:-5] + "Chars"
    
    map24315 = {"key24315": b24315}
    c24315 = map24315["key24315"]
    d24315 = c24315[:-1]
    e24315 = base64.b64decode(base64.b64encode(d24315.encode())).decode()
    f24315 = e24315.split(" ")[0]
    
    thing = ThingFactory.createThing()
    g24315 = "barbarians_at_the_gate"
    bar = thing.doSomething(g24315)

    file_name = None
    fos = None

    try:
        file_name = os.path.join(TESTFILES_DIR, secure_filename(bar))
        fos = open(file_name, 'w')
        response += f"Now ready to write to file: {file_name}"

    except Exception as e:
        print(f"Couldn't open FileOutputStream on file: '{file_name}'")
    finally:
        if fos:
            fos.close()

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
