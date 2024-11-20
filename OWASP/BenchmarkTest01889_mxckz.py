#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 614, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01889.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/field/constructors.tmt with name class_with_nested_string_initialization_positive
#Used extensions:
#Program:
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
            nsh = NestedStringHolder(sql)
            sql = nsh.get_value()
            count = statement.execute(sql)
            statement.connection.commit()
            return "Update complete"
        except sqlite3.Error as e:
            return "Error processing request.", 500

def do_something(request, param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
