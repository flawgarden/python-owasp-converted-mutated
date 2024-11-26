#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#Snyk original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563, 89]
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest00771.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/pm.tmt with name pattern_matching_simple_1_positive
#Used extensions:
#Program:
from typing import Any
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

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00771", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = []
    values = request.args.getlist("BenchmarkTest00771")
    param = values[0] if values else ""

    bar = "safe!"
    map49960 = {}
    map49960["keyA-49960"] = "a-Value"
    map49960["keyB-49960"] = param
    map49960["keyC"] = "another-Value"
    bar = map49960["keyB-49960"]

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        response = cursor.fetchall()
        return render_template("results.html", results=response)
    except sqlite3.Error as e:
        bar = simplePatternMatchingString1(bar)
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simplePatternMatchingString1(obj: Any) -> str:
    match obj:
        case str():
            return obj.upper()
        case _:
            return ""



def simplePatternMatchingString2(obj: Any) -> str:
    match obj:
        case str() if len(obj) > 5:
            return obj.upper()
        case _:
            return ""
