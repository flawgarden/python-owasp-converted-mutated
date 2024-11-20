#Bearer original results: [78]
#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#-------------
#Bearer analysis results: [78]
#Snyk analysis results: []
#CodeQL analysis results: [563, 497, 209]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01938.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_merge_1_positive 
#Used extensions: 
#Program:
from GenericClass import *
from SuperClass import *
from SuperInterface import *
from BinaryOpInterface import *
from UnaryOpClass import *
from UnaryOpInterface import *
from ImplBinaryOpInterfaceClass import *
from BaseBinaryOpClass import *
from DerivedBinaryOpClass import *
from ArrayHolder import *
from StaticFieldHolder import *
from StringFactory import *
from NestedFields import *
from StringHolder import *
from NestedStringHolder import *
from InstanceInitializer import *
from Imports import *
from ReflectionHelper import *
from MagicClass import *
from Record import *
from UnaryOpMutationInterface import *
from MonkeyClass import *
from Exceptions import *
from ClassWrappers import *
from Concurrency import *
from Duck import *

import os
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01938", methods=['GET', 'POST'])
def benchmark_test_01938():
    if request.method == 'GET':
        return benchmark_test_01938_post()

    return benchmark_test_01938_post()

def benchmark_test_01938_post():
    response = app.response_class()
    param = request.headers.get("BenchmarkTest01938", "")

    param = os.path.normpath(param)

    bar = do_something(param)

    cmd = ""
    a1 = ""
    a2 = ""
    args = None
    os_name = os.name

    if os_name == 'nt':
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = "echo "
        args = [a1, a2, cmd + bar]
    else:
        a1 = "sh"
        a2 = "-c"
        cmd = "ls "  # Adjust based on actual function if needed
        args = [a1, a2, cmd + bar]

    args_env = {"foo": "bar"}

    try:
        p = os.popen(" ".join(args), "r")
        output = p.read()
        return output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        return str(e)

def do_something(param):
    map111 = dict()
    map222 = dict()
    map111["lnuaw"] = param
    map222["xqlps"] = param
    map111.update(map222)
    param = map111["xqlps"]
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
