#CodeQL original results: [89]
#Semgrep original results: [89]
#Bearer original results: []
#Snyk original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02628.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/pm.tmt with name pattern_matching_simple_1_negative 
#Used extensions: 
#Program:
from typing import Any
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
from flask import Flask, request, render_template, jsonify
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02628", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02628="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02628' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = simplePatternMatchingString1("zoylh")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "{call " + bar + "}"

    try:
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return jsonify(results)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    bar = "safe!"
    map_23653 = {}
    map_23653["keyA-23653"] = "a-Value"
    map_23653["keyB-23653"] = param
    map_23653["keyC"] = "another-Value"
    bar = map_23653["keyB-23653"]
    
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simplePatternMatchingString1(obj: Any) -> str:
    match obj:
        case str():
            return obj.upper()
        case _:
            return ""



def simplePatternMatchingString2(obj: Any) -> str:
    match obj:
        case str() if len(obj) > 5:
            return obj.upper()
        case _:
            return ""
