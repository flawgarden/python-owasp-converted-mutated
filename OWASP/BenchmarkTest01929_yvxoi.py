#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#-------------
#Bearer analysis results: [78]
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01929.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/monkey/patching.tmt with name monkey_patch_module_function_positive
#Used extensions:
#Program:
import string
from string import capwords
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
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01929", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest01929' in request.headers:
        param = request.headers['BenchmarkTest01929']

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    a1, a2 = ("cmd.exe", "/c") if os.name == 'nt' else ("sh", "-c")
    args = [a1, a2, "echo " + bar]

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - subprocess error")
        raise e

    return response

def do_something(request, param):
    bar = "safe!"
    map44 = {}
    map44["keyA-44"] = "a-Value"
    map44["keyB-44"] = param
    map44["keyC"] = "another-Value"
    bar = map44["keyB-44"]
    originalCapwords = string.capwords
    string.capwords = mock_capwords
    string.capwords = originalCapwords
    bar = string.capwords(bar)

    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')




def newGetArg(self):
    return "fixed_string"





def newGetArgWithArg(self, arg):
    return self.arg + arg





def mock_capwords(s, sep=None):
    return "FIXED_STRING"





def new_arg(arg):
    return arg
