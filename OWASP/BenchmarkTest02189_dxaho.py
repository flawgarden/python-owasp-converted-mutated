#Snyk original results: [643]
#CodeQL original results: [643]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: [79]
#Snyk analysis results: [611]
#CodeQL analysis results: [643, 79, 116]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest02189.py
#Original file CWE's: [643]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_simple_get_1_positive 
#Used extensions: MACRO_Create_Map -> ~[MACRO_MapName]~ = dict() | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234
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
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import ParseError

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest02189", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02189', "")
        bar = do_something(request, param)

        try:
            tree = ET.parse('static/employees.xml')
            root = tree.getroot()
            expression = f"./Employee[@emplid='{bar}']"

            node_list = root.findall(expression)

            response_content = "Your query results are: <br/>"
            for value in node_list:
                response_content += f"{value.text}<br/>"
            return response_content
        except (ET.ParseError, Exception) as e:
            return f"Error parsing XPath input: '{escape_html(bar)}'", 500

    return render_template("index.html")

def do_something(request, param):
    bar = param
    map787234 = dict()
    map787234["koqmm"] = bar
    bar = map787234["koqmm"]
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
