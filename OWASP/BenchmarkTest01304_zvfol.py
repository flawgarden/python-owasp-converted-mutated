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
#Original file name: OWASP/BenchmarkTest01304.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/varargs/varargs.tmt with name varargs_get_first_string_from_array_positive 
#Used extensions: 
#Program:
from typing import TypeVar
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

def get_sql_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/sqli-02/BenchmarkTest01304", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = request.args.get("BenchmarkTest01304", "")
    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME=? and PASSWORD='{bar}'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        return print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

def print_results(statement, sql, response):
    results = statement.fetchall()
    for row in results:
        response.data += str(row)
    return response

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        bar = getFirstStringFromArray(bar, bar)
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
