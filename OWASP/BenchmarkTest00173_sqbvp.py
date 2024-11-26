#Snyk original results: [78]
#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#-------------
#Snyk analysis results: [78]
#Bearer analysis results: [79]
#CodeQL analysis results: [563, 78, 88]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00173.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/list.tmt with name list_clear_start_negative
#Used extensions: MACRO_Create_List -> ~[MACRO_ListName]~ = [] | MACRO_Add_VAR_ToList -> ~[MACRO_ListName]~.append(~[VAR_~[TYPE@1]~@1]~) | MACRO_ListName -> list787231 | MACRO_ListName -> list787231 | MACRO_ListName -> list787231 | MACRO_ListName -> list787231
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
from flask import Flask, request, Response, render_template
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00173", methods=['GET', 'POST'])
def benchmark_test_00173():
    if request.method == 'GET':
        return benchmark_test_00173_post()

    return benchmark_test_00173_post()

def benchmark_test_00173_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if request.headers.get("BenchmarkTest00173") is not None:
        param = request.headers.get("BenchmarkTest00173")

    param = urllib.parse.unquote(param)

    bar = "safe!"
    map68097 = {
        "keyA-68097": "a-Value",
        "keyB-68097": param,
        "keyC": "another-Value"
    }
    bar = map68097["keyB-68097"]

    cmd = get_insecure_os_command_string()
    list787231 = []
    list787231.append(bar)
    list787231.clear()
    bar = list787231[0]

    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        results = p.read()
        print_os_command_results(results, response)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = escape_html(str(e))
        return response

    return response

def get_insecure_os_command_string():
    # Replace with actual command retrieval logic as per your requirements
    return "your-command-here"

def print_os_command_results(results, response):
    response.data = results

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
