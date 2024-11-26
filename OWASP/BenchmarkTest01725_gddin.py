#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01725.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_remove_1_negative
#Used extensions: MACRO_Create_Map -> ~[MACRO_MapName]~ = dict() | MACRO_Add_EXPR_ToMap -> ~[MACRO_MapName]~[~[EXPR_~[TYPE@1]~@1]~] = ~[EXPR_~[TYPE@2]~@2]~ | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234 | MACRO_MapName -> map787234
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
from urllib.parse import unquote
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-03/BenchmarkTest01725", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest01725="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest01725' in query string."

    param = query_string[param_loc + len(paramval):]  # 1st assume "BenchmarkTest01725" param is last
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = unquote(param)
    bar = Test().do_something(param)

    sql = "SELECT USERNAME FROM USERS WHERE USERNAME='foo' AND PASSWORD='{}' LIMIT 1".format(bar)
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        result = cursor.fetchone()
        conn.close()

        if result:
            return "Your results are: " + result[0]
        return "No results returned for query: " + sql

    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        # Simulate the interaction with the Thing interface
        map787234 = dict()
        map787234[10886] = "zuduf"
        map787234[10886] = param
        if 10886 in map787234:
            map787234.pop(10886)
        value7843 = map787234.get(10886)
        if value7843 is None:
            value7843 = "bfbkq"
        param = value7843
        bar = self.some_processing(param)
        return bar

    def some_processing(self, param):
        # Add actual processing logic here if necessary
        return param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
