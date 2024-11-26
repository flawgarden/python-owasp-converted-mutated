#Snyk original results: [78]
#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#-------------
#Snyk analysis results: [79, 78]
#Bearer analysis results: []
#CodeQL analysis results: [563, 209, 497, 88, 78]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01938.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/if.tmt with name if_else_operator_neutral 
#Used extensions: EXPR_bool -> isinstance(~[VAR_SuperClass]~, SubClass)
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

@app.route("/cmdi-02/BenchmarkTest01938", methods=['GET', 'POST'])
def benchmark_test_01938():
    if request.method == 'GET':
        return benchmark_test_01938_post()

    return benchmark_test_01938_post()

def benchmark_test_01938_post():
    response = app.response_class()
    param = request.headers.get("BenchmarkTest01938", "")

    param = os.path.normpath(param)

    bar = do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        tmpUnique42 = bar
        if isinstance(app, SubClass):
            bar = tmpUnique42
        else:
            bar = ""
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "  # Adjust based on actual function if needed
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        p = os.popen(" ".join(args), "r")
        output = p.read()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
