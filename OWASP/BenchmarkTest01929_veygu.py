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
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01929", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest01929' in request.headers:
        param = request.headers['BenchmarkTest01929']
    gen = simple_generator(param, "nenfw", "ssetf")
    genToList = list(gen)
    param = genToList[1]

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    a1, a2 = ("cmd.exe", "/c") if os.name == 'nt' else ("sh", "-c")
    args = [a1, a2, "echo " + bar]

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - subprocess error")
        raise e

    return response

def do_something(request, param):
    bar = "safe!"
    map44 = {}
    map44["keyA-44"] = "a-Value"
    map44["keyB-44"] = param
    map44["keyC"] = "another-Value"
    bar = map44["keyB-44"]

    return bar

if __name__ == '__main__':
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
