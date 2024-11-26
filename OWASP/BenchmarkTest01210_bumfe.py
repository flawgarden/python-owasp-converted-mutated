#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#Snyk original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01210.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/comprehension.tmt with name nested_list_comprehension_positive 
#Used extensions: 
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
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01210", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest01210")
    
    if headers:
        param = headers  # just grab first element

    # URL Decode the header value
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        tmpList = [[connection], [5308], [25038]]
        compList = [x for x in tmpList]
        connection = compList[0][0]
        statement = connection.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql)
    except sqlite3.Error as e:
        return "Error processing request."

class Test:

    def do_something(self, param):
        bar = "safe!"
        map_ = {}
        map_['keyA-86576'] = "a-Value"  # put some stuff in the collection
        map_['keyB-86576'] = param  # put it in a collection
        map_['keyC'] = "another-Value"  # put some stuff in the collection
        bar = map_['keyB-86576']  # get it back out

        return bar

def get_sql_connection():
    return sqlite3.connect('your_database.db')

def print_results(statement, sql):
    # placeholder function to print results
    print("Executing SQL:", sql)
    print("Results:", statement.fetchall())

if __name__ == "__main__":
    app.run(host='0.0.0.0')
