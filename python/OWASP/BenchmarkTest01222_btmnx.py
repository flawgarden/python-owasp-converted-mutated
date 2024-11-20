#Bearer original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Snyk original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: [89]
#CodeQL analysis results: [563, 89]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: []
#Original file name: OWASP/BenchmarkTest01222.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/switch.tmt with name switch_operator_any_positive 
#Used extensions: MACRO_Any_str -> ~[VAR_str]~
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
from flask import Flask, request, render_template, Response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01222", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest01222' in request.headers:
        param = request.headers['BenchmarkTest01222']  # just grab the first element

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)
    tmpUnique42 = param
    match app:
        case "lzhcg":
            param = param
        case _:
            param = tmpUnique42

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

    try:
        connection = sqlite3.connect('database.db')  # Use appropriate database
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        response.data = "Update complete: " + sql
    except sqlite3.Error as e:
        response.data = "Error processing request."
        if not app.config.get('HIDE_SQL_ERRORS', False):
            raise e
    return response

class Test:
    def do_something(self, param):
        bar = "safe!"
        map_ = {}
        map_["keyA-25738"] = "a-Value"  # put some stuff in the collection
        map_["keyB-25738"] = param  # put it in a collection
        map_["keyC"] = "another-Value"  # put some stuff in the collection
        bar = map_.get("keyB-25738")  # get it back out

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
