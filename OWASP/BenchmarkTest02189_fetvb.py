#Snyk original results: [643]
#CodeQL original results: [643]
#Bearer original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [611]
#Bearer analysis results: [79]
#CodeQL analysis results: [116, 79, 643]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest02189.py
#Original file CWE's: [643]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/varargs/varargs.tmt with name varargs_get_string_with_index_negative
#Used extensions:
#Program:
from typing import TypeVar
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
from xml.etree.ElementTree import ParseError

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest02189", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02189', "")
        bar = do_something(request, param)
        bar = getStringWithIndex(1, bar, "hknit")

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
    return bar

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
