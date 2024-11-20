#Snyk original results: [79]
#CodeQL original results: [79]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02608.py
#Original file CWE's: [79]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_cath_negative
#Used extensions: EXPR_str -> ""
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

import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-05/BenchmarkTest02608", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_text = "text/html;charset=UTF-8"
    query_string = request.query_string.decode()
    try:
        raise Exception1("")
    except Exception1 as e:
        response_text = ""
    paramval = "BenchmarkTest02608="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02608' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    response = app.response_class(response=f"Parameter value: {bar}", content_type=response_text)
    response.headers["X-XSS-Protection"] = "0"
    return response

def do_something(param):
    bar = param
    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
