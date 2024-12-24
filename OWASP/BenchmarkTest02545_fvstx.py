from typing import Any
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

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-05/BenchmarkTest02545", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_post(request)
    return handle_get()

def handle_get():
    return handle_post(request)

def handle_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.form.getlist('BenchmarkTest02545')
    values = simplePatternMatchingString2(values)
    param = values[0] if values else ""

    bar = do_something(request, param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

    try:
        conn, cursor = get_sql_statement()
        count = cursor.execute(sql)
        conn.commit()
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def do_something(request, param):
    num = 106
    return param if (7 * 42) - num <= 200 else "This should never happen"

def output_update_complete(sql, response):
    response.data = f"Update complete: {sql}"
    return response

if __name__ == '__main__':
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
