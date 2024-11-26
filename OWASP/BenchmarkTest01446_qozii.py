#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01446.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/virtuality/class.tmt with name base_binary_op_negative 
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
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def decode_param(param):
    if param is not None:
        return param.encode('utf-8').decode('base64')
    return ""

@app.route("/cmdi-01/BenchmarkTest01446", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        param = ""
        flag = True
        for name in request.args:
            values = request.args.getlist(name)
            if values:
                for value in values:
                    if value == 'BenchmarkTest01446':
                        param = name
                        a12341 = BaseBinaryOpClass()
                        param = a12341.virtual_call(param, param)
                        flag = False
                        break

        bar = decode_param(param)

        cmd = ""
        if os.name == 'nt':
            cmd = "echo"

        args_env = {"Foo": "bar"}
        try:
            process = os.popen(f'{cmd} {bar}', 'r')
            results = process.read()
            return render_template("result.html", results=results)
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return render_template("error.html", message=str(e))
        
if __name__ == "__main__":
    app.run(host='0.0.0.0')
