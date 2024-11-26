#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02432.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/field/constructors.tmt with name string_factory_negative
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
import subprocess

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02432", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get("BenchmarkTest02432", default="", type=str)

        bar = do_something(request, param)
        sf = StringFactory.create_instance()
        bar = sf.val

        cmd = ""
        a1 = ""
        a2 = ""
        args = []
        os_name = subprocess.run(['uname'], stdout=subprocess.PIPE).stdout.decode().strip()

        if "Windows" in os_name:
            a1 = "cmd.exe"
            a2 = "/c"
            cmd = "echo "
            args = [a1, a2, cmd + bar]
        else:
            a1 = "sh"
            a2 = "-c"
            cmd = "ls "
            args = [a1, a2, cmd + bar]

        args_env = {"foo": "bar"}

        try:
            result = subprocess.run(args, env=args_env, cwd=".", check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output = result.stdout.decode()
            return output
        except subprocess.CalledProcessError as e:
            return render_template("error.html", error_message=str(e))

def do_something(request, param):
    bar = "safe!"
    map15850 = {
        "keyA-15850": "a-Value",
        "keyB-15850": param,
        "keyC": "another-Value"
    }
    bar = map15850.get("keyB-15850")
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
