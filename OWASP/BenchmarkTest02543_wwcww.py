#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02543.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/lambdas/mutation.tmt with name nested_unary_lambda_mutation_positive
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

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02543", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.form.getlist("BenchmarkTest02543")
    param = values[0] if values else ""

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('your_database.db')  # Update with your database path
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        print_results(rows, response)
        conn.close()
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def do_something(param):
    s23423 = param
    a12341 = StringHolder()
    def lmd(s: StringHolder) -> None:
        def innerLmd(p: StringHolder) -> None:
            p.value = "";
        innerLambda = UnaryOpMutation(innerLmd)
        innerLambda.mutate(s)
        s.value = s23423
    lambda1231 = UnaryOpMutation(lmd)
    lambda1231.mutate(a12341)
    param = a12341.value
    bar = ""

    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"

    return bar

def print_results(rows, response):
    output = "<table><tr><th>Username</th><th>Password</th></tr>"
    for row in rows:
        output += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
    output += "</table>"
    response.data = output

if __name__ == "__main__":
    app.run(host='0.0.0.0')
