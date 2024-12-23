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

import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02324", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = ""
        flag = True
        names = request.args.keys()
        for name in names:
            set787231 = set()
            set787231.add(app)
            app = next(iter(set787231))
            if flag:
                values = request.args.getlist(name)
                if values is not None:
                    for value in values:
                        if value == "BenchmarkTest02324":
                            param = name
                            flag = False

        bar = do_something(param)

        response = app.response_class(
            response=f"Formatted like: {bar} and b.",
            status=200,
            mimetype='text/html'
        )
        response.headers["X-XSS-Protection"] = "0"
        return response
    return render_template("index.html")

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        sbxyz12198 = list(param)
        sbxyz12198[-1] = 'Z'
        bar = ''.join(sbxyz12198)
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
