#Snyk original results: [78]
#Bandit original results: [78]
#Bearer original results: []
#CodeQL original results: []
#Semgrep original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [79]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [78, 605]
#Original file name: OWASP/BenchmarkTest02344.py
#Original file CWE's: [78]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/queue.tmt with name queue_poll_negative 
#Used extensions: MACRO_Create_Queue -> ~[MACRO_QueueName]~ = Queue() | MACRO_Add_CONST_ToQueue -> ~[MACRO_QueueName]~.put_nowait(~[CONST_~[TYPE@1]~]~) | MACRO_Add_CONST_ToQueue -> ~[MACRO_QueueName]~.put_nowait(~[CONST_~[TYPE@1]~]~) | MACRO_Add_Fixed_VAR_ToQueue -> ~[MACRO_QueueName]~.put(~[VAR_~[TYPE@1]~@1]~) | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231
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

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/cmdi-02/BenchmarkTest02344", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    flag = True
    names = request.args.to_dict()
    for name, values in names.items():
        if flag:
            for value in values:
                if value == "BenchmarkTest02344":
                    param = name
                    flag = False
                    break

    bar = do_something(param)
    queue787231 = Queue()
    queue787231.put_nowait("glzzq")
    queue787231.put_nowait("xafdd")
    queue787231.put(bar)
    bar = queue787231.get()

    cmd = get_insecure_os_command_string()
    args_env = [bar]

    try:
        p = os.popen(f"{cmd} {' '.join(args_env)}")
        output = p.read()
        response.data = output
    except Exception as e:
        print("Problem executing cmdi - TestCase")
        response.data = escape_html(str(e))
        return response

    return response

def do_something(param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def get_insecure_os_command_string():
    # Assuming this method is defined in your helper
    return "your_insecure_os_command"

def escape_html(text):
    # Replace special HTML characters to avoid XSS
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
