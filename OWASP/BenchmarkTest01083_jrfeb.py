#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [89]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01083.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/varargs/varargs.tmt with name varargs_get_first_string_positive 
#Used extensions: 
#Program:
from typing import TypeVar
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

@app.route("/sqli-02/BenchmarkTest01083", methods=['GET', 'POST'])
def benchmark_test_01083():
    if request.method == 'GET':
        return benchmark_test_01083_post()
    return benchmark_test_01083_post()

def benchmark_test_01083_post():
    param = request.headers.get("BenchmarkTest01083", "")

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"
    sql = getFirstString(sql, "jmxuk")

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.execute(sql, ("foo",))
        rows = statement.fetchall()
        return render_template("results.html", results=rows)
    except sqlite3.Error as e:
        return "Error processing request."

class Test:

    def do_something(self, param):
        return param

if __name__ == "__main__":
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
