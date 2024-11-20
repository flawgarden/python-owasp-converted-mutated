#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [78, 79]
#CodeQL analysis results: [209, 497]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02147.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/monkey/patching.tmt with name monkey_patch_module_function_negative 
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
from flask import Flask, request, Response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/cmdi-02/BenchmarkTest02147", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    param = request.args.get("BenchmarkTest02147", "")
    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "  # Windows

    try:
        process = os.popen(cmd + bar)
        output = process.read()
        return Response(output, content_type='text/html;charset=UTF-8')
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return Response(str(e), content_type='text/html;charset=UTF-8')


def do_something(param):
    string.capwords = mock_capwords
    param = string.capwords(param)
    return param


if __name__ == "__main__":
    app.run(host='0.0.0.0')




def newGetArg(self):
    return "fixed_string"





def newGetArgWithArg(self, arg):
    return self.arg + arg





def mock_capwords(s, sep=None):
    return "FIXED_STRING"





def new_arg(arg):
    return arg

