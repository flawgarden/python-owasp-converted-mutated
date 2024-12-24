from GenericClass import *
from SuperClass import *
from SuperInterface import *
from BinaryOpInterface import *
from UnaryOpClass import *
from UnaryOpInterface import *
from ImplBinaryOpInterfaceClass import *
from BaseBinaryOpClass import *
from DerivedBinaryOpClass import *
from ArrayHolder import *
from StaticFieldHolder import *
from StringFactory import *
from NestedFields import *
from StringHolder import *
from NestedStringHolder import *
from InstanceInitializer import *
from Imports import *
from ReflectionHelper import *
from MagicClass import *
from Record import *
from UnaryOpMutationInterface import *
from MonkeyClass import *
from Exceptions import *
from ClassWrappers import *
from Concurrency import *
from Duck import *

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
    gen = generator_from(param, "zqpiw", "wraty", "hcrab")
    genToList = list(gen)
    param = genToList[0]

    bar = param
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



def simple_generator(arg1, arg2, arg3):
    yield arg1
    yield arg2
    yield arg3



def infinite_gen(arg1, arg2):
    yield arg1
    while True:
        yield arg2



def generator_from(arg1, arg2, arg3, arg4):
    yield from simple_generator(arg1, arg2, arg3)
    yield arg4
