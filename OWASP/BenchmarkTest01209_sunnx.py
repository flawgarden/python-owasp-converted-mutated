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

import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01209", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_post_request(request)
    else:
        return handle_get_request(request)

def handle_get_request(request):
    return handle_post_request(request)

def handle_post_request(request):
    response = app.response_class(mimetype='text/html;charset=UTF-8')

    param = ''
    if 'BenchmarkTest01209' in request.headers:
        param = request.headers['BenchmarkTest01209']

    param = urllib.parse.unquote(param)

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql, response)
    except Exception as e:
        response.data = b"Error processing request."
        return response

    return response

class Test:
    def do_something(self, request, param):
        bar = ""
        if param is not None:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)

            bar = values_list[0]
        value = None
        bar = bar if value is not None else "acdwr"
        return bar

def get_sql_connection():
    return sqlite3.connect("your_database.db")

def print_results(statement, sql, response):
    rows = statement.fetchall()
    response.data = str(rows).encode('utf-8')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def get_value(value=None):
    if value is None:
        value = "fixed_string"
    return value



def get_value_two_args(arg1, arg2=None):
    if arg2 is None:
        arg1 = "fixed_string"
    return arg1
