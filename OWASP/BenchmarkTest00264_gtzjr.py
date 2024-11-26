#Snyk original results: [22]
#CodeQL original results: [22]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [23]
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest00264.py
#Original file CWE's: [22]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_cath_negative
#Used extensions: EXPR_str -> ""
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
from flask import Flask, request, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-00/BenchmarkTest00264", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ''
    headers = request.headers.getlist("BenchmarkTest00264")

    if headers:
        param = headers[0]

    param = urllib.parse.unquote(param)
    try:
        raise Exception1("")
    except Exception1 as e:
        param = ""

    bar = None
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    file_name = None

    try:
        file_name = os.path.join('path_to_testfiles_directory', bar)
        with open(file_name, 'rb') as fis:
            b = fis.read(1000)
            response.data = (
                "The beginning of file: '"
                + urllib.parse.quote(file_name)
                + "' is:\n\n"
                + urllib.parse.quote(b.decode('utf-8', errors='ignore'))
            )
    except Exception as e:
        response.data = (
            "Problem getting FileInputStream: "
            + urllib.parse.quote(str(e))
        )

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
