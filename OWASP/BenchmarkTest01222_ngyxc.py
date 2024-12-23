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
from flask import Flask, request, render_template, Response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01222", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    if 'BenchmarkTest01222' in request.headers:
        param = request.headers['BenchmarkTest01222']  # just grab the first element
    value = None
    param = param if value is not None else "ytcjm"

    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

    try:
        connection = sqlite3.connect('database.db')  # Use appropriate database
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        response.data = "Update complete: " + sql
    except sqlite3.Error as e:
        response.data = "Error processing request."
        if not app.config.get('HIDE_SQL_ERRORS', False):
            raise e
    return response

class Test:
    def do_something(self, param):
        bar = "safe!"
        map_ = {}
        map_["keyA-25738"] = "a-Value"  # put some stuff in the collection
        map_["keyB-25738"] = param  # put it in a collection
        map_["keyC"] = "another-Value"  # put some stuff in the collection
        bar = map_.get("keyB-25738")  # get it back out

        return bar

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
