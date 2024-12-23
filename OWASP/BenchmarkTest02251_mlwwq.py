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

@app.route("/cmdi-02/BenchmarkTest02251", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02251', '')

    bar = do_something(param)

    cmd = ""
    os_name = os.name

    if os_name == 'nt':  # Windows
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = 'echo'
        args = [a1, a2, cmd, bar]
    else:  # Unix
        a1 = "sh"
        a2 = "-c"
        cmd = f'ping -c1 '
        args = [a1, a2, cmd + bar]

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)

    return response

def do_something(param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    tmpUnique42 = bar
    for el in param:
        bar = tmpUnique42
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
