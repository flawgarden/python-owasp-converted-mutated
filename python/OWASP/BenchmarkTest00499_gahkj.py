#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00499.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/lambdas/mutation.tmt with name nested_unary_lambda_mutation_positive 
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
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00499", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
        
    response = Response(content_type="text/html;charset=UTF-8")
    param = request.args.get("BenchmarkTest00499", "")

    bar = param

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "cmd /c echo "
    s23423 = bar
    a12341 = StringHolder()
    def lmd(s: StringHolder) -> None:
        def innerLmd(p: StringHolder) -> None:
            p.value = "";
        innerLambda = UnaryOpMutation(innerLmd)
        innerLambda.mutate(s)
        s.value = s23423
    lambda1231 = UnaryOpMutation(lmd)
    lambda1231.mutate(a12341)
    bar = a12341.value

    args_env = {"Foo": "bar"}
    
    try:
        process = os.popen(cmd + bar)
        result = process.read()
        response.data = result
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Simple way to return error message
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
