#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: [78, 209, 79, 1004]
#Bearer analysis results: [1004]
#CodeQL analysis results: [563, 497, 209, 78, 88]
#Semgrep analysis results: [489, 614, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00981.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/list.tmt with name list_add_get_at_zero_index_empty_negative 
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
from flask import Flask, request, render_template, make_response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class Test:

    def doSomething(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

@app.route("/cmdi-01/BenchmarkTest00981", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00981.html"))
        user_cookie = make_response("Set a cookie for the test")
        user_cookie.set_cookie("BenchmarkTest00981", ".", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie("BenchmarkTest00981", ".", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response
    
    if request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        
        if 'BenchmarkTest00981' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest00981'])
        
        bar = Test().doSomething(param)

        cmd = ""
        list787231 = []
        list787231.append(bar)
        list787231.insert(0, "")
        bar = list787231[0]
        a1 = ""
        a2 = ""
        args = []
        os_name = os.name

        if os_name == "nt":
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = "echo "
            args = [a1, a2, cmd + bar]
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = "ls "  # or any suitable command
            args = [a1, a2, cmd + bar]

        args_env = {"foo": "bar"}

        try:
            process = os.popen(" ".join(args))
            result = process.read()
            return result
        except Exception as e:
            return f"Problem executing cmd - TestCase: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
