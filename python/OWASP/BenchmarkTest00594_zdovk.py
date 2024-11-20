#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [89]
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest00594.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/record/record.tmt with name nested_record_negative 
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

import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00594", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest00594":
                    param = name
                    flag = False
                    break
        first = SimpleRecord(param)
        second = SimpleRecord("")
        nested = NestedRecord(first, second)
        param = nested.b.t
        if not flag:
            break

    bar = "safe!"
    map29056 = {
        "keyA-29056": "a-Value",
        "keyB-29056": param,
        "keyC": "another-Value"
    }
    bar = map29056["keyB-29056"]

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='{}'".format(bar)

    try:
        connection = sqlite3.connect('database.db')  # Adjust connection method as needed
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        connection.close()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
