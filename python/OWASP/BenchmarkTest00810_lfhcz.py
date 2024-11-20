#Snyk original results: [79]
#CodeQL original results: [79]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest00810.py
#Original file CWE's: [79]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/magic/magic.tmt with name magic_method_repr_positive 
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

from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/xss-01/BenchmarkTest00810", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()


def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00810="
    mc = MagicClass(query_string)
    query_string = repr(mc)
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00810' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)

    bar = param + "_SafeStuff"
    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0')
