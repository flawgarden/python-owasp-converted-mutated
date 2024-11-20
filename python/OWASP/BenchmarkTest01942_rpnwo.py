#Bearer original results: [78]
#Snyk original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#-------------
#Bearer analysis results: [78]
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 78, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01942.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/field/staticField.tmt with name class_with_static_string_field_negative 
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
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01942", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.headers.get("BenchmarkTest01942", "")

        param = param # URL decoding is handled by Flask

        bar = do_something(param)

        cmd = ""
        os_name = os.name
        if os_name == 'nt':
            cmd = 'echo '  # Mimicking the Java command

        args_env = {"Foo": "bar"}
        
        try:
            process = os.popen(cmd + bar)
            result = process.read()
            response.set_data(result)
            return response
        except Exception as e:
            print("Problem executing cmdi - TestCase")
            response.set_data(str(e))
            return response
    return render_template("index.html")

def do_something(param):
    bar = param
    sfh = StaticFieldHolder()
    bar = sfh.value
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
