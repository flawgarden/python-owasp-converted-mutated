#Bearer original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Snyk original results: []
#-------------
#Bearer analysis results: [89]
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01090.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/magic/magic.tmt with name magic_method_repr_positive
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


@app.route("/sqli-02/BenchmarkTest01090", methods=['POST', 'GET'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get("BenchmarkTest01090", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        print_results(sql, results)
    except sqlite3.Error:
        return "Error processing request.", 500

def print_results(sql, results):
    print("SQL: ", sql)
    print("Results: ", results)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_holder = {}
        map_holder["keyA-12212"] = "a-Value"
        map_holder["keyB-12212"] = param
        map_holder["keyC"] = "another-Value"
        bar = map_holder.get("keyB-12212")
        mc = MagicClass(bar)
        bar = repr(mc)
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
