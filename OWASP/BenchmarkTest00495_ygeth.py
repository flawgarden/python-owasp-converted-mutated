#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: [78]
#Bearer analysis results: []
#CodeQL analysis results: [88, 78]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00495.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/list.tmt with name list_to_array_and_get_positive 
#Used extensions: MACRO_Create_List -> ~[MACRO_ListName]~ = [] | MACRO_Add_VAR_ToList -> ~[MACRO_ListName]~.append(~[VAR_~[TYPE@1]~@1]~) | MACRO_ListName -> list787231 | MACRO_ListName -> list787231 | MACRO_ListName -> list787231
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

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00495", methods=['GET', 'POST'])
def benchmark_test_00495():
    if request.method == 'GET':
        return benchmark_test_00495_post()

    return benchmark_test_00495_post()

def benchmark_test_00495_post():
    param = request.args.get('BenchmarkTest00495', '')

    bar = ''
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    list787231 = []
    list787231.append(bar)
    bar = list(list787231)[0]

    cmd = 'your_command_here'  # Placeholder for code to get insecure command string
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        result = process.read()
        return render_template("result.html", result=result)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return render_template("error.html", error=str(e))

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
