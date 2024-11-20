#Snyk original results: [79]
#CodeQL original results: [79]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [116, 79]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest01592.py
#Original file CWE's: [79]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/tuples.tmt with name empty_tuple_operation_negative 
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

from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xss-03/BenchmarkTest01592", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response_content = "text/html;charset=UTF-8"
    values = request.values.getlist("BenchmarkTest01592")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    headers = {"X-XSS-Protection": "0"}
    return bar, response_content, headers

class Test:

    def do_something(self, param):
        empty_tuple = ()
        if len(empty_tuple) == 0:
            empty_tuple += (param, "zvlom")
        param = empty_tuple[1]
        bar = ""
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
