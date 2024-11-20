#Snyk original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#CodeQL original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01383.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/generators.tmt with name generator_infinite_negative
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
app.config['DEBUG'] = True

def get_sql_connection():
    # Replace with your database configuration
    conn = sqlite3.connect('your_database.db')
    return conn

@app.route("/sqli-02/BenchmarkTest01383", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest01383", default="", type=str)

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        with closing(get_sql_connection()) as connection:
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            print_results(results, sql)
    except Exception as e:
        return "Error processing request."

class Test:
    def do_something(self, request, param):
        # Assuming a function that does some processing
        return self.process_param(param)

    def process_param(self, param):
        gen = infinite_gen(param, "kkzgx")
        genToList = [next(gen) for _ in range(1000)]
        param = genToList[1000]
        # Dummy processing logic for demonstration
        return param

def print_results(results, sql):
    # Replace with your logic to display the SQL results
    for row in results:
        print(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simple_generator(arg1, arg2, arg3):
    yield arg1
    yield arg2
    yield arg3



def infinite_gen(arg1, arg2):
    yield arg1
    while True:
        yield arg2



def generator_from(arg1, arg2, arg3, arg4):
    yield from simple_generator(arg1, arg2, arg3)
    yield arg4
