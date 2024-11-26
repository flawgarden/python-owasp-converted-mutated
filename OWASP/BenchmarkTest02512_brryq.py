#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [79]
#CodeQL analysis results: [209, 497]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02512.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/reflection/reflection.tmt with name simple_reflection_negative 
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

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02512", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest02512")
    param = values[0] if values else ""

    bar = do_something(param)

    cmd = get_insecure_os_command_string()
    args = [cmd]
    args_env = [bar]

    try:
        p = os.popen(' '.join(args) + ' ' + ' '.join(args_env))
        response = print_os_command_results(p)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response = escape_html(str(e))
    return response

def do_something(param):
    bar = ""
    try:
        rh = ReflectionHelper.__new__(ReflectionHelper)
        ReflectionHelper.__init__(rh, param)
        setattr(rh, "value", "cfpfd")
        param = rh.get_value()
    except Exception:
        raise
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def get_insecure_os_command_string():
    # Implementation to get the command string
    return "insecure_command"

def print_os_command_results(process):
    return process.read()

def escape_html(string):
    return string.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
