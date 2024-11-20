#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [1004]
#CodeQL analysis results: [209, 497, 88, 78]
#Semgrep analysis results: [489, 614, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00983.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/set.tmt with name set_add_simple_negative
#Used extensions: MACRO_Create_Set -> ~[MACRO_SetName]~ = set() | MACRO_Add_Fixed_CONST_ToSet -> ~[MACRO_SetName]~.add(~[VAR_~[TYPE@1]~@1]~) | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231
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


@app.route("/cmdi-01/BenchmarkTest00983", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("cmdi-01/BenchmarkTest00983.html"))
        user_cookie = make_response("FOO=echo Injection")
        user_cookie.set_cookie("BenchmarkTest00983", "FOO%3Decho+Injection", max_age=60 * 3, secure=True)
        response.set_cookie("BenchmarkTest00983", "FOO%3Decho+Injection", max_age=60 * 3, secure=True)
        return response
    else:
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest00983' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest00983'])
        set787231 = set()
        set787231.add(param)
        param = next(iter(set787231))

        bar = Test().do_something(request, param)

        cmd = "your_command_here"  # Replace with your command retrieval logic

        args_env = [bar]
        try:
            process = os.popen(f"{cmd} {' '.join(args_env)}")
            output = process.read()
            return output
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            return str(e)


class Test:

    def do_something(self, request, param):
        num = 196
        if (500 / 42) + num > 200:
            return param
        else:
            return "This should never happen"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
