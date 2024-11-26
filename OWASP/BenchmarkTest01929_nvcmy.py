#Bearer original results: [78]
#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Snyk original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563, 88, 78]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest01929.py
#Original file CWE's: [78]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/queue.tmt with name simple_peek_negative
#Used extensions: MACRO_Create_Queue -> ~[MACRO_QueueName]~ = PriorityQueue() | MACRO_Add_Fixed_VAR_ToQueue -> ~[MACRO_QueueName]~.put_nowait(~[VAR_~[TYPE@1]~@1]~) | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231
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
from flask import Flask, request, render_template, Response
import urllib.parse

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest01929", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest01929' in request.headers:
        param = request.headers['BenchmarkTest01929']
    queue787231 = PriorityQueue()
    queue787231.put_nowait(param)
    queue787231.get()
    param = queue787231.get_nowait()

    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    a1, a2 = ("cmd.exe", "/c") if os.name == 'nt' else ("sh", "-c")
    args = [a1, a2, "echo " + bar]

    try:
        p = os.popen(' '.join(args))
        output = p.read()
        response.set_data(output)
    except Exception as e:
        print("Problem executing cmdi - subprocess error")
        raise e

    return response

def do_something(request, param):
    bar = "safe!"
    map44 = {}
    map44["keyA-44"] = "a-Value"
    map44["keyB-44"] = param
    map44["keyC"] = "another-Value"
    bar = map44["keyB-44"]

    return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
