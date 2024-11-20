#Snyk original results: [22]
#CodeQL original results: [22]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [79]
#CodeQL analysis results: [22, 36, 73, 23, 99]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02032.py
#Original file CWE's: [22]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_simple_get_1_positive
#Used extensions: MACRO_Create_Map -> ~[MACRO_MapName]~ = dict() | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234
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
import os
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/pathtraver-02/BenchmarkTest02032", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    elif request.method == 'POST':
        response = Response()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = ""
        headers = request.headers.getlist("BenchmarkTest02032")

        if headers:
            param = headers[0]  # just grab first element

        param = urllib.parse.unquote(param)

        bar = do_something(param)

        file_name = None
        try:
            file_name = os.path.join("path_to_test_files_directory", bar)  # adjust path accordingly
            with open(file_name, 'rb') as fis:
                b = fis.read(1000)
                response.data = (
                    f"The beginning of file: '{escape(file_name)}' is:\n\n" +
                    escape(b.decode('utf-8', errors='ignore'))
                )
        except Exception as e:
            print(f"Couldn't open FileInputStream on file: '{file_name}'")

        return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        map787234 = dict()
        map787234["gixlv"] = param
        param = map787234["gixlv"]
        bar = param
    else:
        bar = "This should never happen"
    return bar

def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
