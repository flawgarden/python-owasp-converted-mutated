from threading import Thread
from Record import *
from Exceptions import *
from Concurrency import *
from Imports import *
from ClassWrappers import *
from MonkeyClass import *
from MagicClass import *
from UnaryOpInterface import *
from BinaryOpInterface import *
from DerivedBinaryOpClass import *
from BaseBinaryOpClass import *
from UnaryOpClass import *
from ImplBinaryOpInterfaceClass import *
from Duck import *
from ReflectionHelper import *
from StringHolder import *
from StringFactory import *
from InstanceInitializer import *
from NestedStringHolder import *
from ArrayHolder import *
from NestedFields import *
from StaticFieldHolder import *
from UnaryOpMutationInterface import *
from GenericClass import *
from SuperInterface import *
from SuperClass import *

from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
w = Wrapper(app)
task = SettingTask(w, "")
task.start()
try:
    task.join()
except RuntimeError:
    pass
app = w.i
app.config['DEBUG'] = True

class Test:

    def do_something(self, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target in ['C', 'D']:
            bar = param
        else:
            bar = "bobs_your_uncle"

        return bar

@app.route("/xss-02/BenchmarkTest01505", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01505", "")
        bar = Test().do_something(param)

        response = "<!DOCTYPE html>\n<html>\n<body>\n<p>"
        response += "Formatted like: %s and %s." % ("a", bar)
        response += "\n</p>\n</body>\n</html>"
        return response
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
