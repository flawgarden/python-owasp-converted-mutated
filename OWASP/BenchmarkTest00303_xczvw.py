#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#-------------
#Snyk analysis results: [209]
#Bearer analysis results: []
#CodeQL analysis results: [563, 88, 78]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest00303.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/exceptions/causeThrows.tmt with name null_pointer_exception_negative
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
import urllib.parse
from flask import Flask, request, render_template, Response
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-00/BenchmarkTest00303", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest00303", "")
    param = urllib.parse.unquote(param)

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    def get_none() -> Any:
        return None
    try:
        a = get_none()
        a = a + a
    except TypeError as e:
        bar = ""

    cmd = ""
    a1 = ""
    a2 = ""
    args = []
    os_name = os.name

    if os_name == 'nt':
        a1 = 'cmd.exe'
        a2 = '/c'
        cmd = f'echo {bar}'
        args = [a1, a2, cmd]
    else:
        a1 = 'sh'
        a2 = '-c'
        cmd = f'ping -c1 {bar}'
        args = [a1, a2, cmd]

    try:
        process = os.popen(' '.join(args))
        results = process.read()
        response.set_data(results)
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.set_data(f'Error: {e}')
        return response

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
