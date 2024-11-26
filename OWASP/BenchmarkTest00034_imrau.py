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
#Original file name: OWASP/BenchmarkTest00034.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/set.tmt with name set_disjoint_positive 
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

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00034", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class()
        response.headers['Content-Type'] = 'text/html;charset=UTF-8'

        param = request.args.get('BenchmarkTest00034', '')
        set111 = set()
        set222 = set()
        set111.add(param)
        set222.add(param)
        value78411 = 0.6171171897731295
        if set111.isdisjoint(set222):
            value78411 = param
        param = value78411

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + param + "'"

        try:
            statement = get_sql_statement()
            statement.execute(sql)
            rows = statement.fetchall()
            # Assuming there's a function to print results
            for row in rows:
                response.data += str(row) + '<br>'
            return response
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
