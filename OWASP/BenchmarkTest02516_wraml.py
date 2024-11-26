#Snyk original results: [78]
#Bearer original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Semgrep original results: []
#-------------
#Snyk analysis results: [78]
#Bearer analysis results: []
#CodeQL analysis results: [563, 78, 88]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02516.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_simple_get_1_positive
#Used extensions: MACRO_Create_Map -> ~[MACRO_MapName]~ = dict() | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234
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

@app.route("/cmdi-02/BenchmarkTest02516", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    else:
        return benchmark_test_post(request)

def benchmark_test_post(request):
    response = app.response_class()
    map787234 = dict()
    map787234["ruizd"] = request
    request = map787234["ruizd"]
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.args.getlist("BenchmarkTest02516")
    param = values[0] if values else ""

    bar = do_something(request, param)

    cmd = get_insecure_os_command_string()
    args_env = [bar]
    try:
        process = os.popen(f"{cmd} {' '.join(args_env)}")
        output = process.read()
        response.data = output
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)
        return response

def do_something(request, param):
    bar = "safe!"
    map74796 = {
        "keyA-74796": "a-Value",
        "keyB-74796": param,
        "keyC": "another-Value"
    }
    bar = map74796["keyB-74796"]
    return bar

def get_insecure_os_command_string():
    # Implement the method to return the insecure OS command string.
    return "echo"  # Example command

if __name__ == "__main__":
    app.run(host='0.0.0.0')
