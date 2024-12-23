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
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01192", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = ""
    headers = request.headers.get("BenchmarkTest01192")

    if headers:
        param = headers  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()

    try:
        p = os.popen(f"{cmd} {bar}")
        response = p.read()
        p.close()
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = str(e)

    return response

class Test:
    def do_something(self, request, param):
        bar = ""

        # Simple if statement that assigns param to bar on true condition
        num = 196
        gen = simple_generator(param, 0.8128400421681531, 0.9860343766534704)
        genToList = list(gen)
        param = genToList[0]
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"

        return bar

def get_insecure_os_command_string():
    return "your_command_here"  # replace with actual command logic

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
