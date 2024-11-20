#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01083.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/interpolation.tmt with name format_method_interpolation_negative 
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
    tmpStr = param
    tmpStr = "ktfrr"
    interpolatedStr = "Some_prefix, {}".format(tmpStr)
    param = interpolatedStr

    bar = Test().do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

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
