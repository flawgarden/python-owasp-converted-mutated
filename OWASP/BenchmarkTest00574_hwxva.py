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

@app.route("/cmdi-00/BenchmarkTest00574", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00574":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    num = 106
    a12341 = ImplBinaryOpInterfaceClass1()
    param = a12341.interface_call("", param)
    bar = param if (7 * 42) - num <= 200 else "This should never happen"

    cmd = os.getenv('INSECURE_OS_COMMAND_STRING')
    args_env = [bar]

    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        output = process.read()
        return output
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
