from typing import Any
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

@app.route("/cmdi-01/BenchmarkTest01285", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.form.get('BenchmarkTest01285', '')

    bar = Test().do_something(request, param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    try:
        os_name = simplePatternMatchingString1("gfxdk")
        process = os.popen(cmd + bar)
        output = process.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

class Test:
    def do_something(self, request, param):
        bar = ""
        if param:
            values_list = []
            values_list.append("safe")
            values_list.append(param)
            values_list.append("moresafe")

            values_list.pop(0)  # remove the 1st safe value

            bar = values_list[0]  # get the param value

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simplePatternMatchingString1(obj: Any) -> str:
    match obj:
        case str():
            return obj.upper()
        case _:
            return ""



def simplePatternMatchingString2(obj: Any) -> str:
    match obj:
        case str() if len(obj) > 5:
            return obj.upper()
        case _:
            return ""
