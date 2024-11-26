#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563, 89]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest00018.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/set.tmt with name set_add_simple_negative 
#Used extensions: MACRO_Create_Set -> ~[MACRO_SetName]~ = set() | MACRO_Add_Fixed_CONST_ToSet -> ~[MACRO_SetName]~.add(~[VAR_~[TYPE@1]~@1]~) | MACRO_SetName -> set787231 | MACRO_SetName -> set787231 | MACRO_SetName -> set787231
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

import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00018", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'
    
    param = ""
    headers = request.headers.getlist("BenchmarkTest00018")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + param + "')"

    try:
        set787231 = set()
        set787231.add(sql)
        sql = next(iter(set787231))
        statement = get_sql_statement()
        count = statement.execute(sql)
        statement.connection.commit() 
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

def output_update_complete(sql, response):
    response.data = f"Update complete for SQL: {sql}"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
