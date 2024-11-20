#Bearer original results: [89]
#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: []
#-------------
#Bearer analysis results: [89]
#Snyk analysis results: [89]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest01208.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/tuples.tmt with name tuple_as_dict_key_negative 
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

@app.route("/sqli-02/BenchmarkTest01208", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01208", "")
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = f"{{call {bar}}}"
    tuple1 = ("aaaa",)
    tuple2 = ("bbbb",)
    my_dict = { (tuple1): sql, (tuple2): "kdzwq" }
    sql = my_dict[("bbbb",)]

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql)
        connection.close()
    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

def print_results(results, sql):
    for row in results:
        print(row)  # or process results as needed

if __name__ == "__main__":
    app.run(host='0.0.0.0')
