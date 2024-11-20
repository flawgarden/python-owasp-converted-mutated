#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Snyk analysis results: [79]
#Bearer analysis results: []
#CodeQL analysis results: [563, 116, 79, 89]
#Semgrep analysis results: [489, 79, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01891.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/varargs/varargs.tmt with name varargs_get_first_string_from_array_positive 
#Used extensions: 
#Program:
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
from flask import Flask, request, render_template, make_response, redirect, url_for
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-04/BenchmarkTest01891", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01891.html"))
        user_cookie = make_response("Set-Cookie: BenchmarkTest01891=bar; Max-Age=180; Secure; Path=" + request.path)
        response.headers.add("Set-Cookie", "BenchmarkTest01891=bar; Max-Age=180; Secure; Path=" + request.path)
        return response

    elif request.method == 'POST':
        the_cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01891' in the_cookies:
            param = urllib.parse.unquote(the_cookies['BenchmarkTest01891'])

        bar = do_something(request, param)
        sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"
        sql = getFirstStringFromArray(sql, "ABC")

        try:
            statement = get_sql_statement()
            statement.execute(sql)
            get_sql_statement().connection.commit()
            output_update_complete(sql)
        except sqlite3.Error as e:
            return "Error processing request."

def do_something(request, param):
    bar = param
    num = 106
    return bar if (7 * 42) - num <= 200 else "This should never happen"

def output_update_complete(sql):
    return f"SQL update complete: {sql}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

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
