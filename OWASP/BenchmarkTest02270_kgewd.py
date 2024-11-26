#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [79, 89]
#Bearer analysis results: []
#CodeQL analysis results: [570, 571, 563]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02270.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/while.tmt with name while_operator_positive
#Used extensions: EXPR_bool -> ~[EXPR_str@1]~ is not None and ~[EXPR_str@1]~[~[CONST_int]~] == ~[CONST_str]~
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
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02270", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response_html = ""
        param = request.values.get("BenchmarkTest02270", "")

        bar = do_something(param)

        sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('your_database.db')
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            response_html = print_results(cursor, sql)
            connection.close()
        except sqlite3.Error as e:
            response_html = "Error processing request."

        return response_html
    return render_template("index.html")

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
    tmpUnique42 = switch_target
    while "uovgg" is not None and "uovgg"[-3734] == "aqpfy":
        switch_target = tmpUnique42
    else:
        bar = "bobs_your_uncle"

    return bar

def print_results(cursor, sql):
    results = cursor.fetchall()
    output = f"<h2>Results for query: {sql}</h2><ul>"
    for row in results:
        output += "<li>" + str(row) + "</li>"
    output += "</ul>"
    return output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
