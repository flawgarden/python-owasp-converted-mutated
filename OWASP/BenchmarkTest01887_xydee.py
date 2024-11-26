#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [1004, 614, 89]
#Bearer analysis results: [1004, 614]
#CodeQL analysis results: [563, 89]
#Semgrep analysis results: [489, 614, 668]
#Bandit analysis results: []
#Original file name: OWASP/BenchmarkTest01887.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/pm.tmt with name pattern_matching_simple_4_negative
#Used extensions:
#Program:
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

import os
from flask import Flask, request, render_template, make_response
from urllib.parse import unquote
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-04/BenchmarkTest01887", methods=['GET', 'POST'])
def benchmark_test():
    app = simplePatternMatchingString2("zxbdg")
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01887.html"))
        user_cookie = make_response("bar")
        user_cookie.set_cookie("BenchmarkTest01887", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie(user_cookie.data)
        return response

    if request.method == 'POST':
        param = "noCookieValueSupplied"
        the_cookies = request.cookies

        if the_cookies:
            param = the_cookies.get("BenchmarkTest01887", param)
            param = unquote(param)

        bar = do_something(param)
        sql = f"INSERT INTO users (username, password) VALUES ('foo', '{bar}')"

        try:
            conn, cursor = get_sql_statement()
            cursor.execute(sql)
            conn.commit()
            return "Update complete", 200
        except sqlite3.Error as e:
            return "Error processing request.", 500

def do_something(param):
    return param

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
