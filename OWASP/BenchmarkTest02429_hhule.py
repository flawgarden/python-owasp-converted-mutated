#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: [209, 79, 78]
#Bearer analysis results: []
#CodeQL analysis results: [563, 88, 78]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: []
#Original file name: OWASP/BenchmarkTest02429.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/switch.tmt with name switch_operator_any_negative 
#Used extensions: MACRO_Any_str -> ~[VAR_str]~
#Program:
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


@app.route("/cmdi-02/BenchmarkTest02429", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = request.args.get("BenchmarkTest02429", "")

    bar = do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo"
        args = [a1, a2, cmd + " " + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ping -c 1 "
        args = [a1, a2, cmd + bar]

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        tmpUnique42 = ""
        match os_name:
            case "jfkwq":
                a1 = ""
            case _:
                a1 = tmpUnique42
        response.set_data(e)
        return response

    return response


def do_something(param):
    thing = create_thing()
    bar = thing.do_something(param)
    return bar


def create_thing():
    # Placeholder for the actual implementation of ThingFactory
    class ThingInterface:
        def do_something(self, param):
            return param  # Placeholder logic

    return ThingInterface()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
