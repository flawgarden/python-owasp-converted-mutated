#Snyk original results: [78]
#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#-------------
#Snyk analysis results: [78]
#Bearer analysis results: []
#CodeQL analysis results: [685]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02150.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/monkey/patching.tmt with name monkey_patch_class_method_with_arg_positive 
#Used extensions: 
#Program:
import string
from string import capwords
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

@app.route("/cmdi-02/BenchmarkTest02150", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post(request)
    return benchmark_test_post(request)

def benchmark_test_post(request):
    MonkeyClass.getArg = newGetArgWithArg
    tmpInstance = MonkeyClass(request)
    request = tmpInstance.getArg("jlxsr")
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest02150", "")
    bar = do_something(request, param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == "nt":
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        process = os.popen(' '.join(args) + ' ' + ' '.join(f'{k}={v}' for k, v in args_env.items()))
        output = process.read()
        response.response = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.response = str(e)
        return response

    return response

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')




def newGetArg(self):
    return "fixed_string"





def newGetArgWithArg(self, arg):
    return self.arg + arg





def mock_capwords(s, sep=None):
    return "FIXED_STRING"





def new_arg(arg):
    return arg

