#Bearer original results: [643]
#Snyk original results: [643]
#CodeQL original results: [643]
#Semgrep original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: [79, 643]
#Snyk analysis results: [611]
#CodeQL analysis results: [563]
#Semgrep analysis results: [79, 668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest01223.py
#Original file CWE's: [643]  
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
import xml.etree.ElementTree as ET
from urllib.parse import unquote


app = Flask(__name__, static_url_path='/static', static_folder='static')


@app.route("/xpathi-00/BenchmarkTest01223", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()


def benchmark_test_post():
    param = ""
    if "BenchmarkTest01223" in request.headers:
        param = request.headers.get("BenchmarkTest01223")  # just grab first element

    param = unquote(param)

    bar = Test().do_something(request, param)

    try:
        tree = ET.parse('employees.xml')
        root = tree.getroot()

        expression = ".//Employee[@emplid='" + bar + "']"
        node_list = root.findall(expression)

        output = "Your query results are: <br/>"
        for value in node_list:
            output += value.text + "<br/>"

        return output
    except ET.ParseError as e:
        return "Error parsing XPath input: '" + escape_html(bar) + "'"


class Test:

    def do_something(self, request, param):
        bar = ""
        guess = "ABC"
        switch_target = guess[2]

        if switch_target == 'A':
            bar = param
        elif switch_target == 'B':
            bar = "bobs_your_uncle"
        elif switch_target == 'C' or switch_target == 'D':
            bar = param
        else:
            bar = "bobs_your_uncle"
        sfh = StaticFieldHolder()
        bar = sfh.value

        return bar


def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
