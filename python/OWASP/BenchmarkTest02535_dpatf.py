#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#Snyk original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: []
#CodeQL analysis results: []
#Semgrep analysis results: [489, 915, 704, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02535.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/field/regularField.tmt with name class_with_string_field_negative 
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

from flask import Flask, request, render_template
import sqlite3
import base64

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02535", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.args.getlist("BenchmarkTest02535")
    param = values[0] if values else ""

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect("your_database.db")
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute(sql, ("foo",))
        results = cursor.fetchall()
        return print_results(results, response)
    except sqlite3.Error as e:
        response.data = b"Error processing request."
        return response

def do_something(param):
    sh = StringHolder()
    sh.value = ""
    param = sh.value
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def print_results(results, response):
    # Assuming you want to format results for your response
    for row in results:
        response.data += f"<p>{dict(row)}</p>".encode()
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
