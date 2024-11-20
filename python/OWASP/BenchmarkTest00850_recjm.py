#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [89]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest00850.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/set.tmt with name set_remove_simple_positive 
#Used extensions: MACRO_Create_Set -> ~[MACRO_SetName]~ = set() | MACRO_Add_Fixed_EXPR_ToSet -> ~[MACRO_SetName]~.add(~[EXPR_~[TYPE@1]~@1]~) | MACRO_Add_Fixed_VAR_ToSet -> ~[MACRO_SetName]~.add(~[VAR_~[TYPE@1]~@1]~) | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231
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

from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00850", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    query_string = request.query_string.decode('utf-8')
    set787231 = set()
    set787231.add("yurqp")
    set787231.add(query_string)
    set787231.remove("yurqp")
    query_string = next(iter(set787231))
    paramval = "BenchmarkTest00850="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00850' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    
    param = urllib.parse.unquote(param)

    bar = ""
    if param is not None:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        results = cursor.fetchall()
        return render_template("results.html", results=results, sql=sql)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
