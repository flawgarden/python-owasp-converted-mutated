#Snyk original results: [78]
#CodeQL original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [497, 209]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01690.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/record/record.tmt with name simple_record_negative 
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
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-01/BenchmarkTest01690", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01690="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval}' in query string."
    
    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    cmd = get_insecure_os_command_string()

    args_env = [bar]
    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        result = p.read()
        p.close()
        return result
    except Exception as e:
        return f"Problem executing cmdi - TestCase: {str(e)}"

class Test:
    def do_something(self, request, param):
        record = SimpleRecord("")
        param = record.t
        bar = param
        return bar

def get_insecure_os_command_string():
    # Replace with the actual logic to retrieve the insecure OS command string
    return "echo"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
