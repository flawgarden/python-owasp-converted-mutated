#Bearer original results: [89]
#Snyk original results: [89]
#CodeQL original results: [89]
#Bandit original results: [89]
#Semgrep original results: []
#-------------
#Bearer analysis results: [89]
#Snyk analysis results: [79]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02181.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/lambdas/mutation.tmt with name unary_lambda_mutation_positive 
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
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_database(sql):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None
    finally:
        conn.close()

@app.route("/sqli-04/BenchmarkTest02181", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get('BenchmarkTest02181', '')
    bar = do_something(request, param)
    s23423 = bar
    a12341 = StringHolder()
    def lmd(s: StringHolder) -> None:
        s.value = s23423
    lambda1231 = UnaryOpMutation(lmd)
    lambda1231.mutate(a12341)
    bar = a12341.value

    sql = f"SELECT userid FROM USERS WHERE USERNAME='foo' AND PASSWORD='{bar}' LIMIT 1"
    try:
        result = query_database(sql)
        return f"Your results are: {result}" if result else "No results returned for query."
    except Exception as e:
        return "Error processing request."

def do_something(request, param):
    return param

if __name__ == '__main__':
    app.run(host='0.0.0.0')