#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [79]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01361.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_remove_1_negative
#Used extensions: MACRO_Create_Map -> ~[MACRO_MapName]~ = dict() | MACRO_Add_EXPR_ToMap -> ~[MACRO_MapName]~[~[EXPR_~[TYPE@1]~@1]~] = ~[EXPR_~[TYPE@2]~@2]~ | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234
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

@app.route("/cmdi-01/BenchmarkTest01361", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html; charset=UTF-8'

    param = request.args.get('BenchmarkTest01361', '')
    map787234 = dict()
    map787234[app] = "qoxxp"
    map787234[app] = param
    if app in map787234:
        map787234.pop(app)
    value7843 = map787234.get(app)
    if value7843 is None:
        value7843 = "dgiad"
    param = value7843

    bar = Test().do_something(param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = escape_for_html(str(e))
        return response

    return response

class Test:

    def do_something(self, param):
        bar = param
        return bar

def get_insecure_os_command_string():
    # Placeholder for the actual implementation to retrieve the OS command string
    return "your_command_here"

def escape_for_html(text):
    # Basic HTML escaping implementation
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
