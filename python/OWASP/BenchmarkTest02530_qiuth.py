#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bearer original results: []
#Bandit original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02530.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/none.tmt with name none_in_function_negative 
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
    param = get_value()
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
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



def get_value(value=None):
    if value is None:
        value = "fixed_string"
    return value



def get_value_two_args(arg1, arg2=None):
    if arg2 is None:
        arg1 = "fixed_string"
    return arg1
