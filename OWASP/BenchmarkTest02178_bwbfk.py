#Bearer original results: [89]
#CodeQL original results: [89]
#Bandit original results: [89]
#Snyk original results: []
#Semgrep original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [79]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 704, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02178.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_merge_2_negative 
#Used extensions: MACRO_Create_Map -> ~[MACRO_MapName]~ = dict() | MACRO_Add_EXPR_ToMap -> ~[MACRO_MapName]~[~[EXPR_~[TYPE@1]~@1]~] = ~[EXPR_~[TYPE@2]~@2]~ | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234
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
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_for_list(sql):
    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        map787234 = dict()
        map787234[14395] = 0.42254446961891856
        map787234[14395] = sql
        if 14395 in map787234:
            map787234.update({14395: 0.46073101196954913})
        sql = map787234[14395]
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return results
    except Exception as e:
        raise e

@app.route("/sqli-04/BenchmarkTest02178", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    param = request.args.get("BenchmarkTest02178", "")
    bar = do_something(param)
    
    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
    try:
        list_results = query_for_list(sql)
        response += "Your results are: <br>"
        for o in list_results:
            response += str(o) + "<br>"
    except Exception as e:
        response += "Error processing request."
    return response

def do_something(param):
    bar = "safe!"
    map38026 = {}
    map38026["keyA-38026"] = "a-Value"
    map38026["keyB-38026"] = param
    map38026["keyC"] = "another-Value"
    bar = map38026["keyB-38026"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
