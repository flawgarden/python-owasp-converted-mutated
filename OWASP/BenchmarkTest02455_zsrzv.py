from typing import Any
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

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor(), conn

@app.route("/sqli-05/BenchmarkTest02455", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    param = request.args.get("BenchmarkTest02455", "")

    bar = do_something(param)
    sql = f"INSERT INTO users (username, password) VALUES ('foo', '{bar}')"

    try:
        statement, conn = get_sql_statement()
        bar = simplePatternMatchingString1("iubam")
        count = statement.execute(sql)
        conn.commit()
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        response.status_code = 500
        return response

    return response

def do_something(param):
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def output_update_complete(sql, response):
    response.data = f"SQL Update Complete: {sql}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def simplePatternMatchingString1(obj: Any) -> str:
    match obj:
        case str():
            return obj.upper()
        case _:
            return ""



def simplePatternMatchingString2(obj: Any) -> str:
    match obj:
        case str() if len(obj) > 5:
            return obj.upper()
        case _:
            return ""
