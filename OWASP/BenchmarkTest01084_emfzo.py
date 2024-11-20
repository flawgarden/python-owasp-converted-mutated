#Snyk original results: [89]
#Bearer original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: [89]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01084.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/import/import.tmt with name import_string_module_alias_negative
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

from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01084", methods=['GET', 'POST'])
def benchmark_test_01084():
    if request.method == 'GET':
        return benchmark_test_01084_post()

    return benchmark_test_01084_post()

def benchmark_test_01084_post():
    response = "text/html;charset=UTF-8"

    param = request.headers.get("BenchmarkTest01084", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect("your_database.db")
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()

        return print_results(cursor, sql)
    except sqlite3.Error as e:
        return "Error processing request."

def print_results(cursor, sql):
    # Mock-up function to simulate the result handling
    return f"Executed SQL: {sql}, Results: {cursor.fetchall()}"

class Test:
    def do_something(self, param):
        s123 = SimpleImportAlias()
        param = s123.func("rrtkb")
        num = 196
        if (500 / 42) + num > 200:
            return param
        return "This should never happen"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
