#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00500.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/virtuality/interface.tmt with name base_binary_op_interface_negative
#Used extensions:
#Program:
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

@app.route("/cmdi-00/BenchmarkTest00500", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()  # Redirect GET requests to POST logic

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ''
    map = request.args
    if map:
        values = map.getlist("BenchmarkTest00500")
        if values:
            param = values[0]

    bar = ""

    num = 196
    a12341 = ImplBinaryOpInterfaceClass1() if num else ImplBinaryOpInterfaceClass2()
    param = a12341.interface_call("", "")
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Adjust command as needed for your environment

    args_env = {"Foo": "bar"}

    try:
        p = os.popen(cmd + bar)  # Execute the command
        output = p.read()  # Get the output from the command
        response.data = output.encode('utf-8')  # Update response with command output
    except Exception as e:
        print("Problem executing cmd - TestCase")
        response.data = str(e).encode('utf-8')
        return response

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
