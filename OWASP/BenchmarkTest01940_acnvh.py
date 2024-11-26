#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: [78]
#CodeQL analysis results: [563, 497, 209]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01940.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/generators.tmt with name generator_infinite_positive 
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
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01940", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_type = "text/html;charset=UTF-8"
    param = request.headers.get("BenchmarkTest01940", "")

    param = param # Assuming param should be URL decoded

    bar = do_something(param)

    cmd = ""
    if os.name == "nt":
        cmd = "echo " # Use equivalent command in Windows
        
    args_env = {"Foo": "bar"}
    try:
        process = os.popen(cmd + bar)  # Note: Using os.popen for demonstration
        output = process.read()
        process.close()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    gen = infinite_gen(bar, "fzpff")
    genToList = [next(gen) for _ in range(5)]
    bar = genToList[0]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simple_generator(arg1, arg2, arg3):
    yield arg1
    yield arg2
    yield arg3



def infinite_gen(arg1, arg2):
    yield arg1
    while True:
        yield arg2



def generator_from(arg1, arg2, arg3, arg4):
    yield from simple_generator(arg1, arg2, arg3)
    yield arg4
