#Bearer original results: [89]
#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest00203.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/field/staticField.tmt with name class_with_static_string_field_negative 
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
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00203", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = request.response
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest00203", "")
    param = urllib.parse.unquote(param)
    sfh = StaticFieldHolder()
    param = sfh.value

    bar = ""
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
        return render_template("success.html", sql=sql)
    except sqlite3.Error as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
