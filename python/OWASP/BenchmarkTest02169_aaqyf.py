#Snyk original results: [89]
#Semgrep original results: [89]
#Bearer original results: []
#CodeQL original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest02169.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/interpolation.tmt with name format_method_interpolation_negative 
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
import sqlite3
from contextlib import closing

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/sqli-04/BenchmarkTest02169", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get('BenchmarkTest02169', "")
        bar = do_something(param)
        tmpStr = bar
        tmpStr = "ltlgt"
        interpolatedStr = "Some_prefix, {}".format(tmpStr)
        bar = interpolatedStr

        sql = "{call " + bar + "}"

        try:
            with closing(database_con()) as connection:
                cursor = connection.cursor()
                cursor.execute(sql)
                rs = cursor.fetchall()
                print_results(rs, sql)
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    return bar

def database_con():
    return sqlite3.connect('your_database.db')

def print_results(rs, sql):
    for row in rs:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
