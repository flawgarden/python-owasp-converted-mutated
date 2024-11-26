#Snyk original results: [89]
#Bearer original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#-------------
#Snyk analysis results: []
#Bearer analysis results: [89]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01209.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/field/constructors.tmt with name class_with_array_initialization_negative 
#Used extensions: MACRO_Empty_String_Array -> ["", "", ""]
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

@app.route("/sqli-02/BenchmarkTest01209", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_post_request(request)
    else:
        return handle_get_request(request)

def handle_get_request(request):
    return handle_post_request(request)

def handle_post_request(request):
    response = app.response_class(mimetype='text/html;charset=UTF-8')

    param = ''
    if 'BenchmarkTest01209' in request.headers:
        param = request.headers['BenchmarkTest01209']

    param = urllib.parse.unquote(param)
    tmpArrayUnique42 = ["", "", ""]
    tmpArrayUnique42[0] = param
    ah = ArrayHolder(values=tmpArrayUnique42)
    param = ah.values[1]

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql, response)
    except Exception as e:
        response.data = b"Error processing request."
        return response

    return response

class Test:
    def do_something(self, request, param):
        bar = ""
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)

            bar = values_list[0]
        return bar

def get_sql_connection():
    return sqlite3.connect("your_database.db")

def print_results(statement, sql, response):
    rows = statement.fetchall()
    response.data = str(rows).encode('utf-8')
    
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
