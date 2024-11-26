#Snyk original results: [79]
#CodeQL original results: [79]
#Semgrep original results: [79]
#Bearer original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [79]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 79, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest01057.py
#Original file CWE's: [79]  
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

import urllib.parse
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-02/BenchmarkTest01057", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("Referer", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    response = make_response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

class Test:

    def do_something(self, request, param):
        string.capwords = mock_capwords
        param = string.capwords(param)
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
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

