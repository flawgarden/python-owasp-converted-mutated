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

@app.route("/cmdi-00/BenchmarkTest00295", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    if 'BenchmarkTest00295' in request.headers:
        param = request.headers['BenchmarkTest00295']
    map787234 = dict()
    map787234["kiyyk"] = param
    if "kiyyk" in map787234:
        param = map787234.pop("kiyyk")

    param = urllib.parse.unquote(param)

    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    os_name = os.name
    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
    else:
        a1 = "sh"
        a2 = "-c"

    args = [a1, a2, "echo " + bar]

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        return output
    except IOError as e:
        print("Problem executing cmdi - subprocess issue")
        return str(e), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
