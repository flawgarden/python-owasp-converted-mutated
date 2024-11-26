#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563, 78, 88]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: []
#Original file name: OWASP/BenchmarkTest01288.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/switch.tmt with name switch_operator_any_positive
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

@app.route("/cmdi-01/BenchmarkTest01288", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.form.get("BenchmarkTest01288", "")
    bar = Test().do_something(param)

    cmd = "your_command_here"  # Replace with the function to get the insecure command string
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(f"{cmd} {bar}")  # You can adapt this to fit your needs
        output = p.read()
        return render_template("index.html", output=output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        tmpUnique42 = param
        match param:
            case "bjyid":
                param = param
            case _:
                param = tmpUnique42
        return render_template("index.html", error=str(e))

class Test:
    def do_something(self, param):
        bar = "safe!"
        map58555 = {
            "keyA-58555": "a-Value",
            "keyB-58555": param,
            "keyC": "another-Value"
        }
        bar = map58555.get("keyB-58555")
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
