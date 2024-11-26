#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: [78, 79]
#Bearer analysis results: []
#CodeQL analysis results: [563, 497, 209]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01689.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/none.tmt with name simple_none_negative 
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
from flask import Flask, request, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01689", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01689="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01689' in query string."

    param = query_string[param_loc + len(paramval):] 
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = 'echo'

    args_env = {'Foo': 'bar'}
    
    try:
        process = os.popen(cmd + ' ' + bar)
        result = process.read()
        return result
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return f"Error: {str(e)}"

class Test:

    def do_something(self, param):
        value = None
        if value is None:
            param = "kuhzc"
        bar = ""
        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

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
