from typing import TypeVar
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
from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Replace with your database
    return conn.cursor()

@app.route("/sqli-04/BenchmarkTest01889", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01889.html"))
        user_cookie = make_response()
        user_cookie.set_cookie("BenchmarkTest01889", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return user_cookie

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies
        if "BenchmarkTest01889" in the_cookies:
            param = urllib.parse.unquote(the_cookies["BenchmarkTest01889"])

        bar = do_something(request, param)

        sql = "INSERT INTO users (username, password) VALUES ('foo', '" + bar + "')"

        try:
            statement = get_sql_statement()
            count = statement.execute(sql)
            statement.connection.commit()
            return "Update complete"
        except sqlite3.Error as e:
            return "Error processing request.", 500

def do_something(request, param):
    bar = param
    bar = getStringWithIndex(0, bar, bar)
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')



def getFirstString(*lines: str) -> str:
    return getStringWithIndex(0, *lines)



def getStringWithIndex(ind: int, *lines: str) -> str:
    return lines[ind]



def getFirstStringFromArray(*lines: str) -> str:
    return list(lines)[0]



TYPEVAR = TypeVar('TYPEVAR')
def varargsWithGenerics(*elements: TYPEVAR) -> TYPEVAR:
    return elements[0]



def combineStrings(*strings: str) -> str:
    return ", ".join(strings)
