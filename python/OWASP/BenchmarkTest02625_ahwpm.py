#CodeQL original results: [89]
#Semgrep original results: [89]
#Snyk original results: []
#Bearer original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02625.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/queue.tmt with name two_queues_positive 
#Used extensions: EXPR_str -> ~[EXPR_str]~[~[EXPR_int]~:~[EXPR_int]~] | EXPR_str -> ~[EXPR_Match]~.group(~[EXPR_int]~) | EXPR_int -> 42
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

from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02625", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02625="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02625' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = sqlite3.connect('database.db')  # Adjust based on your database configuration
        sourceQueue = SimpleQueue()
        targetQueue = SimpleQueue()
        sourceQueue.put("pvprl")
        sourceQueue.put("tfoil")
        targetQueue.put(sql)
        targetQueue.put(ampersand_loc.group(param_loc)[42:28371])
        while not sourceQueue.empty():
            targetQueue.put(sourceQueue.get())
        sql = targetQueue.get()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return str(results)  # or format results as needed
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = "safe!"
    map_82391 = {
        "keyA-82391": "a-Value",
        "keyB-82391": param,
        "keyC": "another-Value"
    }
    bar = map_82391.get("keyB-82391")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
