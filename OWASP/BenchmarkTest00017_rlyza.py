#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#Semgrep original results: []
#-------------
#Bearer analysis results: [79]
#Snyk analysis results: [79, 78]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00017.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/duck/typing.tmt with name duck_typing_quack_method_negative
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
import urllib.parse
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00017", methods=['GET', 'POST'])
def benchmark_test_00017():
    if request.method == 'GET':
        return benchmark_test_00017_post()

    return benchmark_test_00017_post()

def benchmark_test_00017_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')
    param = ""

    headers = request.headers.getlist("BenchmarkTest00017")
    if headers:
        param = headers[0]  # just grab first element
    duck_like = NotADuck()
    param = make_it_quack(duck_like, param)

    param = urllib.parse.unquote(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':  # Windows
        cmd = "cmd /c echo "  # substitute with appropriate command

    try:
        p = os.popen(cmd + param)
        result = p.read()
        response.set_data(result)
        return response
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(str(e).replace("<", "&lt;").replace(">", "&gt;"))
        return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def make_it_quack(duck, arg):
    return duck.quack(arg)



def make_it_quack_attr(duck, arg):
    if hasattr(duck, 'quack'):
        return duck.quack(arg)
    return "fixed string"



def add_quack_method(duck):
    duck.quack = lambda a: "Some_ prefix " + a



def make_it_quack_field_attr(duck, arg):
    if hasattr(duck, 'constant'):
        return duck.quack(arg)
    else:
        return "fixed_string"
