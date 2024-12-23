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

from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-04/BenchmarkTest02409", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    param = request.args.get("BenchmarkTest02409", "")
    bar = do_something(param)
    map787234 = dict()
    map787234["ubwtt"] = "wrnpl"
    map787234["ubwtt"] = bar
    if "ubwtt" in map787234:
        map787234.pop("ubwtt")
    value7843 = map787234.get("ubwtt")
    if value7843 is None:
        value7843 = "pjsje"
    bar = value7843

    response = Response(bar, content_type="text/html;charset=UTF-8")
    response.headers["X-XSS-Protection"] = "0"
    return response

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
