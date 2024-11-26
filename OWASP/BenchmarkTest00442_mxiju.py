#Snyk original results: [643]
#CodeQL original results: [643]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [611, 643]
#Bearer analysis results: []
#CodeQL analysis results: [570, 561, 571]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest00442.py
#Original file CWE's: [643]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/record/record.tmt with name nested_record_positive 
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
from flask import Flask, request, render_template
import xml.etree.ElementTree as ET
from xml.sax.saxutils import escape

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00442", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = ""
    param = request.form.get("BenchmarkTest00442", "")
    
    bar = param if (7 * 42) - 106 <= 200 else "This should never happen"
    
    try:
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        expression = "./Employee[@emplid='{}']".format(bar)
        first = SimpleRecord(expression)
        second = SimpleRecord("")
        nested = NestedRecord(first, second)
        expression = nested.a.t
        result = root.findall(expression)

        response += "Your query results are: " + str([ET.tostring(emp) for emp in result]) + "<br/>"

    except ET.ParseError as e:
        response += "Error parsing XPath input: '" + escape(bar) + "'"
        raise Exception(e)
    
    return render_template("response.html", response=response)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
