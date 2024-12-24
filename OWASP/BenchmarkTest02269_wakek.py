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
from contextlib import closing

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    connection = sqlite3.connect('database.db')  # Update database path accordingly
    return connection

def print_results(statement, sql, response):
    results = statement.fetchall()
    for row in results:
        response.write(str(row) + "<br>")  # Format the result as needed

@app.route("/sqli-04/BenchmarkTest02269", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    response = request.response
    response.headers['Content-Type'] = "text/html;charset=UTF-8"

    param = request.values.get('BenchmarkTest02269', '')

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        with closing(get_sql_connection()) as connection:
            statement = connection.cursor()
            statement.execute(sql, ('foo',))  # The first parameter is always 'foo'
            print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.write("Error processing request.")

    return response

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    record = SimpleRecord("")
    bar = record.t
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
