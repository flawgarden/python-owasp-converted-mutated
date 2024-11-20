#Snyk original results: [79]
#CodeQL original results: [79]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [79]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02324.py
#Original file CWE's: [79]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/record/record.tmt with name nested_record_negative 
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

@app.route("/xss-04/BenchmarkTest02324", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = ""
        flag = True
        names = request.args.keys()
        for name in names:
            if flag:
                values = request.args.getlist(name)
                if values is not None:
                    for value in values:
                        if value == "BenchmarkTest02324":
                            param = name
                            flag = False

        bar = do_something(param)
        first = SimpleRecord(bar)
        second = SimpleRecord("")
        nested = NestedRecord(first, second)
        bar = nested.b.t

        response = app.response_class(
            response=f"Formatted like: {bar} and b.", 
            status=200,
            mimetype='text/html'
        )
        response.headers["X-XSS-Protection"] = "0"
        return response
    return render_template("index.html")

def do_something(param):
    bar = param
    if param is not None and len(param) > 1:
        sbxyz12198 = list(param)
        sbxyz12198[-1] = 'Z'
        bar = ''.join(sbxyz12198)
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
