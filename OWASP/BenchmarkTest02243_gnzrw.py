#CodeQL original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#Bearer original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563, 209, 497]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02243.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/lambdas/mutation.tmt with name unary_lambda_mutation_positive
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
import os
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02243", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02243', '')
        s23423 = param
        a12341 = StringHolder()
        def lmd(s: StringHolder) -> None:
            s.value = s23423
        lambda1231 = UnaryOpMutation(lmd)
        lambda1231.mutate(a12341)
        param = a12341.value

        bar = do_something(param)

        arg_list = []
        os_name = os.name
        if os_name == 'nt':
            arg_list.append("cmd.exe")
            arg_list.append("/c")
        else:
            arg_list.append("sh")
            arg_list.append("-c")

        arg_list.append("echo " + bar)

        try:
            result = subprocess.run(arg_list, capture_output=True, text=True)
            return result.stdout
        except Exception as e:
            print("Problem executing cmdi - subprocess Test Case")
            return str(e)

    return render_template("index.html")

def do_something(param):
    bar = "safe!"
    map_19941 = {}
    map_19941["keyA-19941"] = "a-Value"
    map_19941["keyB-19941"] = param
    map_19941["keyC"] = "another-Value"
    bar = map_19941["keyB-19941"]

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
