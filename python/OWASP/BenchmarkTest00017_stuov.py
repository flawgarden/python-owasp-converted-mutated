#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [79]
#CodeQL analysis results: [78, 88]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00017.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/none.tmt with name conditional_expression_none_positive 
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
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00017", methods=['GET', 'POST'])
def benchmark_test_00017():
    if request.method == 'GET':
        return benchmark_test_00017_post()

    return benchmark_test_00017_post()

def benchmark_test_00017_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = ""
    
    headers = request.headers.getlist("BenchmarkTest00017")
    value = None
    headers = headers if value is None else "ixrvj"
    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "cmd /c echo "  # substitute with appropriate command

    try:
        p = os.popen(cmd + param)
        result = p.read()
        response.set_data(result)
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e).replace("<", "&lt;").replace(">", "&gt;"))
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def get_value(value=None):
    if value is None:
        value = "fixed_string"
    return value



def get_value_two_args(arg1, arg2=None):
    if arg2 is None:
        arg1 = "fixed_string"
    return arg1