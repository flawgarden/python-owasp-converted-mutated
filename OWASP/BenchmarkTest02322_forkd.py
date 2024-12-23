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
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02322", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = ""
        flag = True
        names = request.args.keys()
        for name in names:
            values = request.values.getlist(name)
            if values is not None:
                for value in values:
                    if value == "BenchmarkTest02322":
                        map787234 = dict()
                        map787234["sypak"] = "quqfb"
                        map787234.setdefault("sypak", app)
                        app = map787234["sypak"]
                        param = name
                        flag = False
                        break
            if not flag:
                break

        bar = do_something(param)

        response = app.response_class(
            response=f"Formatted like: {bar} and b.",
            status=200,
            mimetype='text/html'
        )
        response.headers['X-XSS-Protection'] = '0'
        return response
    return render_template("index.html")

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
