#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [89, 1004]
#Bearer analysis results: [1004]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 614, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01888.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/conditional/for.tmt with name for_operator_negative 
#Used extensions: EXPR_int -> ~[EXPR_int]~ + ~[EXPR_int]~ | EXPR_int -> -1
#Program:
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

@app.route("/sqli-04/BenchmarkTest01888", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01888.html"))
        user_cookie = make_response("bar")
        user_cookie.set_cookie(key="BenchmarkTest01888", value="bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        response.set_cookie(user_cookie.key, user_cookie.value, max_age=user_cookie.max_age, secure=user_cookie.secure, path=user_cookie.path, domain=user_cookie.domain)
        return response
    else:
        param = "noCookieValueSupplied"
        if request.cookies.get("BenchmarkTest01888"):
            param = urllib.parse.unquote(request.cookies.get("BenchmarkTest01888"))

        bar = do_something(request, param)
        sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

        try:
            connection = sqlite3.connect('database.db')  # Replace with your database path
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            return "Update complete", 200
        except sqlite3.Error as e:
            return "Error processing request.", 500

def do_something(request, param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    for i in range(-1 + request):
        bar = ""
    else:
        bar = "This should never happen"
    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
