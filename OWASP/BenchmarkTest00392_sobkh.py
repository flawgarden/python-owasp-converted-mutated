#Snyk original results: [79]
#CodeQL original results: [79]
#Semgrep original results: [79]
#Bearer original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 79, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest00392.py
#Original file CWE's: [79]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/list.tmt with name list_set_negative 
#Used extensions: MACRO_Create_List -> ~[MACRO_ListName]~ = [] | MACRO_Add_CONST_ToList -> ~[MACRO_ListName]~.append(~[CONST_~[TYPE@1]~@1]~) | MACRO_ListName -> list787231 | MACRO_ListName -> list787231 | MACRO_ListName -> list787231 | MACRO_ListName -> list787231
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
from flask import Flask, request, make_response

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-00/BenchmarkTest00392", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00392', '')
    
    bar = param
    if param and len(param) > 1:
        sbxyz38384 = list(param)
        bar = ''.join(sbxyz38384[:-1] + ['Z'])
    list787231 = []
    list787231.append("pnbhh")
    tmp1232141245 = list787231[0]
    list787231[0] = bar
    bar = tmp1232141245

    response = make_response(bar)
    response.headers["X-XSS-Protection"] = "0"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
