#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bearer original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [89]
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02530.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/field/constructors.tmt with name class_with_nested_string_initialization_positive
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
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02530", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return benchmark_post()
    else:
        return benchmark_post()

def benchmark_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    values = request.values.getlist("BenchmarkTest02530")
    param = values[0] if values else ""

    bar = do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql)
        rs = statement.fetchall()
        print_results(rs, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response
    return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    nsh = NestedStringHolder(bar)
    bar = nsh.get_value()
    return bar

def get_sql_connection():
    return sqlite3.connect('your_database.db')

def print_results(rs, sql, response):
    for row in rs:
        response.data += str(row) + "<br>"
    response.data += f"Executed SQL: {sql}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
