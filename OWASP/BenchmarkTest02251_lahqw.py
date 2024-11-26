#CodeQL original results: [78]
#Semgrep original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02251.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/queue.tmt with name simple_poll_negative 
#Used extensions: MACRO_Create_Queue -> ~[MACRO_QueueName]~ = PriorityQueue() | MACRO_Add_EXPR_ToQueue -> ~[MACRO_QueueName]~.put_nowait(~[EXPR_~[TYPE@1]~]~) | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | EXPR_bool -> ~[EXPR_str]~.startswith(~[EXPR_str]~)
#Program:
from queue import SimpleQueue, Queue, PriorityQueue
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

@app.route("/cmdi-02/BenchmarkTest02251", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02251', '')

    bar = do_something(param)

    cmd = ""
    os_name = os.name
    queue787231 = PriorityQueue()
    queue787231.put_nowait("xmkrk".startswith("whhtn"))
    bar = queue787231.get()

    if os_name == 'nt':  # Windows
        a1 = "cmd.exe"
        a2 = "/c"
        cmd = 'echo'
        args = [a1, a2, cmd, bar]
    else:  # Unix
        a1 = "sh"
        a2 = "-c"
        cmd = f'ping -c1 '
        args = [a1, a2, cmd + bar]

    try:
        process = os.popen(" ".join(args))
        output = process.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = str(e)

    return response

def do_something(param):
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
