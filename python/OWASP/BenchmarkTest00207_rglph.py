#Bearer original results: [643]
#CodeQL original results: [643]
#Snyk original results: []
#Semgrep original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [611]
#Bearer analysis results: []
#CodeQL analysis results: [79, 116, 643]
#Semgrep analysis results: [489, 79, 668]
#Bandit analysis results: [20, 605]
#Original file name: OWASP/BenchmarkTest00207.py
#Original file CWE's: [643]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/queue.tmt with name simple_peek_negative 
#Used extensions: MACRO_Create_Queue -> ~[MACRO_QueueName]~ = PriorityQueue() | MACRO_Add_Fixed_VAR_ToQueue -> ~[MACRO_QueueName]~.put(~[VAR_~[TYPE@1]~@1]~) | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231
#Program:
from queue import SimpleQueue, Queue, PriorityQueue
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
import base64
import xml.etree.ElementTree as ET

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/xpathi-00/BenchmarkTest00207", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest00207', '')
    param = param.encode('utf-8').decode('unicode_escape')
    
    bar = ''
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    try:
        tree = ET.parse('employees.xml')
        queue787231 = PriorityQueue()
        queue787231.put(bar)
        queue787231.get()
        bar = queue787231.get_nowait()
        xml_document = tree.getroot()

        expression = f".//Employee[@emplid='{bar}']"
        result = xml_document.findall(expression)

        response_text = "Your query results are: " + ', '.join([ET.tostring(emp).decode() for emp in result]) + "<br/>"
        return response_text

    except Exception as e:
        return f"Error parsing XPath input: '{bar}'"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
