#Snyk original results: [79]
#CodeQL original results: [79]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [79]
#CodeQL analysis results: []
#Semgrep analysis results: [668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02591.py
#Original file CWE's: [79]
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

import urllib.parse
from flask import Flask, request

app = Flask(__name__)

@app.route("/xss-05/BenchmarkTest02591", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response_data = "text/html;charset=UTF-8"
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02591="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02591' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = f'Content-Type: {response_data}\n'
    response += 'X-XSS-Protection: 0\n'
    response += f'Formatted like: {bar} and b.'

    return response

def do_something(param):
    sbxyz9811 = str(param)
    originalCapwords = string.capwords
    string.capwords = mock_capwords
    string.capwords = originalCapwords
    sbxyz9811 = string.capwords(sbxyz9811)
    bar = sbxyz9811 + "_SafeStuff"
    return bar

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
