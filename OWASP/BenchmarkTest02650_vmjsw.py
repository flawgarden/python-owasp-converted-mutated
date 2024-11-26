#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: []
#CodeQL analysis results: [89]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02650.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/set.tmt with name set_remove_simple_positive
#Used extensions: MACRO_Create_Set -> ~[MACRO_SetName]~ = set() | MACRO_Add_Fixed_EXPR_ToSet -> ~[MACRO_SetName]~.add(~[EXPR_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_VAR_ToSet -> ~[MACRO_SetName]~.add(~[VAR_~[TYPE@1]~@1]~) | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231
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

from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-06/BenchmarkTest02650", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    param_val = "BenchmarkTest02650="
    param_loc = query_string.find(param_val)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02650' in query string."

    param = query_string[param_loc + len(param_val):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(param_val):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('your_database.db')  # Replace with your database path
        cursor = conn.cursor()
        set787231 = set()
        set787231.add("kascd")
        set787231.add(sql)
        set787231.remove("kascd")
        sql = next(iter(set787231))
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return str(results)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
