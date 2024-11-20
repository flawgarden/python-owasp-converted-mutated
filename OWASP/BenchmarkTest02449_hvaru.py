#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bearer original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02449.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/field/regularField.tmt with name class_with_string_field_negative
#Used extensions:
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

import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-05/BenchmarkTest02449", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""

    param = request.args.get("BenchmarkTest02449", "")
    bar = do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = get_sql_connection()
        sh = StringHolder()
        sh.value = ""
        sql = sh.value
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        response = print_results(results, sql)
    except sqlite3.Error as e:
        response += "Error processing request."

    return response

def do_something(param):
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

def get_sql_connection():
    return sqlite3.connect('database.db')

def print_results(results, sql):
    output = f"<h1>SQL Query: {sql}</h1><ul>"
    for row in results:
        output += "<li>" + str(row) + "</li>"
    output += "</ul>"
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
