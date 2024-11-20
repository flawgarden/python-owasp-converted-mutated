#Snyk original results: [643]
#Bearer original results: [643]
#CodeQL original results: [643]
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [643, 611]
#Bearer analysis results: [79]
#CodeQL analysis results: [563]
#Semgrep analysis results: [668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest01223.py
#Original file CWE's: [643]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/exceptions/tryCatchFinally.tmt with name try_cath_negative 
#Used extensions: EXPR_str -> ~[EXPR_str]~.lower() | EXPR_str -> ~[EXPR_str]~ + ~[EXPR_str]~
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
    try:
        raise Exception1("ucllg" + "leppw".lower())
    except Exception1 as e:
        param = ""

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

        return bar


def escape_html(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;").replace("'", "&#x27;")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
