#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [79, 89]
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01716.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/record/record.tmt with name nested_record_positive
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
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01716", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return 'Method not allowed', 405

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest01716="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return f"getQueryString() couldn't find expected parameter '{paramval[:-1]}' in query string.", 400

    param = query_string[param_loc + len(paramval):].split('&')[0]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME=? and PASSWORD='{bar}'"

    try:
        first = SimpleRecord(sql)
        second = SimpleRecord("")
        nested = NestedRecord(first, second)
        sql = nested.a.t
        connection = get_sql_connection()
        statement = connection.execute(sql, ("foo",))
        results = statement.fetchall()
        return print_results(results, sql)
    except Exception as e:
        return "Error processing request.", 500

class Test:
    def do_something(self, param):
        num = 196
        if (500 / 42) + num > 200:
            return param
        return "This should never happen"

def get_sql_connection():
    return sqlite3.connect('your_database.db')

def print_results(results, sql):
    return f"Executed SQL: {sql}, Results: {results}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
