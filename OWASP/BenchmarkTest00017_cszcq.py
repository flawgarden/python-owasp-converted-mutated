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
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00017", methods=['GET', 'POST'])
def benchmark_test_00017():
    if request.method == 'GET':
        return benchmark_test_00017_post()

    return benchmark_test_00017_post()

def benchmark_test_00017_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = ""

    headers = request.headers.getlist("BenchmarkTest00017")
    if headers:
        param = headers[0]  # just grab first element
    set787231 = set()
    set787231.add(param)
    param = next(iter(set787231))

    param = urllib.parse.unquote(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "cmd /c echo "  # substitute with appropriate command

    try:
        p = os.popen(cmd + param)
        result = p.read()
        response.set_data(result)
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e).replace("<", "&lt;").replace(">", "&gt;"))
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
