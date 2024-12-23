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

from flask import Flask, request, Response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01417", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest01417":
                    param = name
                    a12341 = ImplBinaryOpInterfaceClass2()
                    param = a12341.interface_call(param, "")
                    flag = False
                    break
        if not flag:
            break

    bar = Test().do_something(request, param)

    response.headers['X-XSS-Protection'] = '0'
    obj = ["a", bar]
    response.set_data("<!DOCTYPE html>\n<html>\n<body>\n<p>" +
                      "Formatted like: %s and %s." % tuple(obj) +
                      "\n</p>\n</body>\n</html>")
    return response

class Test:
    def do_something(self, request, param):
        bar = param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
