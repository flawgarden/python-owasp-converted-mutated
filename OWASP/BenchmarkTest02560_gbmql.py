#Snyk original results: [22]
#Bearer original results: [22]
#CodeQL original results: [22]
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [22]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: []
#Original file name: OWASP/BenchmarkTest02560.py
#Original file CWE's: [22]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/pm.tmt with name pattern_matching_simple_1_negative
#Used extensions:
#Program:
from typing import Any
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

@app.route("/pathtraver-03/BenchmarkTest02560", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)

    return benchmark_test_post(request)

def benchmark_test_post(request):
    response = {}
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02560="
    query_string = simplePatternMatchingString1("ykuva")
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        response['message'] = f"getQueryString() couldn't find expected parameter '{paramval}'."
        return response

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = param

    bar = do_something(request, param)

    file_name = None
    try:
        file_name = os.path.join("testfiles_dir", bar)  # Assuming 'testfiles_dir' is defined
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response['file_content'] = f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
    except Exception as e:
        response['message'] = f"Problem getting File: {str(e)}"

    return response

def do_something(request, param):
    bar = param
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simplePatternMatchingString1(obj: Any) -> str:
    match obj:
        case str():
            return obj.upper()
        case _:
            return ""



def simplePatternMatchingString2(obj: Any) -> str:
    match obj:
        case str() if len(obj) > 5:
            return obj.upper()
        case _:
            return ""
