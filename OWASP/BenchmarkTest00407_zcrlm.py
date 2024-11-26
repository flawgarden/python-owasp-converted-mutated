#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: [78]
#Bearer analysis results: []
#CodeQL analysis results: [563, 88, 78]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: []
#Original file name: OWASP/BenchmarkTest00407.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/switch.tmt with name switch_operator_negative
#Used extensions:
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
from flask import Flask, request, render_template, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-00/BenchmarkTest00407", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.content_type = "text/html;charset=UTF-8"

    param = request.form.get("BenchmarkTest00407", "")

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)
        bar = values_list[0]

    cmd = ""
    a1 = ""
    tmpUnique42 = ""
    match a1:
        case "":
            pass
        case "bqklv":
            a1 = ""
        case _:
            a1 = tmpUnique42
    a2 = ""
    args = None
    os_name = os.name

    if os_name == "nt":
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
