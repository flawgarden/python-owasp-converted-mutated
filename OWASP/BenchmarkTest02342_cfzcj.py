#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#-------------
#Snyk analysis results: [78]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 78, 668]
#Original file name: OWASP/BenchmarkTest02342.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/generators.tmt with name generator_yield_from_negative 
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

from flask import Flask, request, render_template
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02342", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02342":
                    param = name
                    flag = False
                    break
        gen = generator_from(param, "pnpfb", "qgrbx", "dwhbl")
        genToList = list(gen)
        param = genToList[2]
        if not flag:
            break

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = subprocess.Popen(cmd + bar, env=args_env, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)  # Use appropriate escaping method if needed.
        return response

    return response

def do_something(param):
    return param

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
