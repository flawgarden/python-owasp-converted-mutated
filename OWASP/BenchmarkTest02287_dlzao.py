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

@app.route("/sqli-05/BenchmarkTest02287", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_post()
    return handle_get()

def handle_get():
    return handle_post()

def handle_post():
    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.form.get('BenchmarkTest02287', '')

    bar = do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','{}')".format(bar)

    try:
        sql = ""
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        count = cursor.execute(sql)
        conn.commit()
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        if hide_sql_errors:
            response.data = "Error processing request."
            return response
        else:
            raise Exception(e)

    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def output_update_complete(sql, response):
    response.data = "Update complete: {}".format(sql)

hide_sql_errors = True

if __name__ == "__main__":
    app.run(host='0.0.0.0')
