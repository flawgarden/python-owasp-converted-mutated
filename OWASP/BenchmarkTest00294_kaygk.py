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
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00294", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    if request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00294", "")
    param = urllib.parse.unquote(param)

    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    argList = []
    osName = os.name
    if osName == 'nt':
        argList.append("cmd.exe")
        argList.append("/c")
    else:
        argList.append("sh")
        argList.append("-c")
    set787231 = set()
    set787231.add("ntrnb")
    set787231.add(bar)
    set787231.remove("ntrnb")
    bar = next(iter(set787231))
    argList.append("echo " + bar)

    try:
        result = os.popen(" ".join(argList)).read()
        return result
    except Exception as e:
        print("Problem executing command")
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
