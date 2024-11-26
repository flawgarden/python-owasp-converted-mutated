#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [79]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02154.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/none.tmt with name none_in_function_with_two_args_positive 
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

@app.route("/cmdi-02/BenchmarkTest02154", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest02154", "")
    bar = do_something(param)

    cmd = ""
    os_name = os.name
    if os_name == 'nt':
        cmd = "echo "

    args_env = {"Foo": "bar"}

    try:
        process = os.popen(cmd + bar)  # Simplified execution for demonstration purposes
        output = process.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(escape_html(str(e)))
        return response

    return response

def do_something(param):
    bar = param
    param = get_value_two_args(app, "1")
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\"", "&quot;").replace("'", "&apos;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def get_value(value=None):
    if value is None:
        value = "fixed_string"
    return value



def get_value_two_args(arg1, arg2=None):
    if arg2 is None:
        arg1 = "fixed_string"
    return arg1
