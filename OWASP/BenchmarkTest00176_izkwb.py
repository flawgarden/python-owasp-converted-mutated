import string
from string import capwords
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

@app.route("/cmdi-00/BenchmarkTest00176", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00176", "")
    param = param.encode().decode('utf-8')

    bar = param
    MonkeyClass.getArg = newGetArg
    tmpInstance = MonkeyClass(bar)
    bar = tmpInstance.getArg()
    cmd = ""
    os_name = os.name

    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        return render_template("output.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error=str(e))

if __name__ == "__main__":
    app.run(host='0.0.0.0')




def newGetArg(self):
    return "fixed_string"





def newGetArgWithArg(self, arg):
    return self.arg + arg





def mock_capwords(s, sep=None):
    return "FIXED_STRING"





def new_arg(arg):
    return arg
