#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563, 497, 209, 88, 78]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00311.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/set.tmt with name set_remove_simple_negative 
#Used extensions: MACRO_Create_Set -> ~[MACRO_SetName]~ = set() | MACRO_Add_Fixed_EXPR_ToSet -> ~[MACRO_SetName]~.add(~[EXPR_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_VAR_ToSet -> ~[MACRO_SetName]~.add(~[VAR_~[TYPE@1]~@1]~) | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231
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

@app.route("/cmdi-00/BenchmarkTest00311", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = "text/html;charset=UTF-8"
    
    param = ""
    headers = request.headers.get("BenchmarkTest00311")

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = ""
    guess = "ABC"
    set787231 = set()
    set787231.add("hbdbc")
    set787231.add(param)
    set787231.remove(param)
    param = next(iter(set787231))
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    cmd = "YOUR_COMMAND_HERE"  # Replace with your command retrieval logic
    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        p.close()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
