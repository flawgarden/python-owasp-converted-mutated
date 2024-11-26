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
#Original file name: OWASP/BenchmarkTest02047.py
#Original file CWE's: [79]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_cath_finally_negative
#Used extensions: EXPR_str -> ~[EXPR_str]~ + ~[EXPR_str]~ | EXPR_str -> ~[EXPR_str]~.replace('/', '.') | EXPR_str -> ""
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

@app.route("/xss-03/BenchmarkTest02047", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    referer = request.headers.get('Referer')

    if referer:
        param = referer

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    response = Response(bar)
    response.headers['X-XSS-Protection'] = '0'
    return response

def do_something(param):
    bar = ""
    tmpUnique42 = param
    try:
        raise Exception1("aczfh".replace('/', '.') + "")
    except Exception1 as e:
        param = tmpUnique42
    finally:
        param = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
