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
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

class DatabaseHelper:
    @staticmethod
    def get_sql_statement():
        conn = sqlite3.connect('example.db')
        return conn.cursor(), conn

    @staticmethod
    def print_results(statement, sql, response):
        results = statement.fetchall()
        for row in results:
            response.write(str(row))

@app.route("/sqli-02/BenchmarkTest01093", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest01093", "")
    param = urllib.parse.unquote(param)
    tmpStr = param
    tmpStr = "cnoof"
    interpolatedStr = f"Some_prefix -> {tmpStr}"
    param = interpolatedStr

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement, conn = DatabaseHelper.get_sql_statement()
        statement.execute(sql)
        DatabaseHelper.print_results(statement, sql, response)
        conn.close()
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map18142 = {}
        map18142["keyA-18142"] = "a-Value"
        map18142["keyB-18142"] = param
        map18142["keyC"] = "another-Value"
        bar = map18142.get("keyB-18142")

        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
