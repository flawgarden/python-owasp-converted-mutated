#Snyk original results: [22]
#CodeQL original results: [22]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563, 23, 99, 22, 36, 73, 79, 116, 497, 209]
#Semgrep analysis results: [668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest00783.py
#Original file CWE's: [22]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/varargs/varargs.tmt with name varargs_get_first_string_from_array_positive
#Used extensions:
#Program:
from typing import TypeVar
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
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/pathtraver-00/BenchmarkTest00783", methods=['GET', 'POST'])
def benchmark_test_00783():
    if request.method == 'GET':
        return benchmark_test_00783_post()

    return benchmark_test_00783_post()

def benchmark_test_00783_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00783="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00783' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map_2299 = {
        "keyA-2299": "a-Value",
        "keyB-2299": param,
        "keyC": "another-Value"
    }
    bar = map_2299["keyB-2299"]
    bar = getFirstStringFromArray(bar, paramval)

    file_name = os.path.join("testfiles", bar)

    try:
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            return f"The beginning of file: '{file_name}' is:\n\n{b.decode('utf-8', errors='ignore')}"
    except Exception as e:
        print(f"Couldn't open file: '{file_name}'")
        return f"Problem getting file: {str(e)}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
