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

import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

def print_results(cursor, sql, response):
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        response.write(str(row))

@app.route("/sqli-04/BenchmarkTest02092", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = request.response
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.getlist("BenchmarkTest02092")

    if headers:
        param = headers[0]

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        print_results(cursor, sql, response)
        conn.close()
    except sqlite3.Error as e:
        response.write("Error processing request.")
        return

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
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)

        bar = values_list[0]

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
