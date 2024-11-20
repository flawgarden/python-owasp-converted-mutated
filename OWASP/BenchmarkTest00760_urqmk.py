#CodeQL original results: [89]
#Semgrep original results: [89]
#Snyk original results: []
#Bearer original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: []
#Bearer analysis results: []
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest00760.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/virtuality/interface.tmt with name impl_binary_op_interface_class2_negative
#Used extensions:
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

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00760", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    values = request.values.getlist("BenchmarkTest00760")
    a12341 = ImplBinaryOpInterfaceClass2()
    values = a12341.interface_call(values[0], "")
    param = values[0] if values else ""

    bar = "safe!"
    map18915 = {}
    map18915["keyA-18915"] = "a-Value"
    map18915["keyB-18915"] = param
    map18915["keyC"] = "another-Value"
    bar = map18915["keyB-18915"]

    sql = "{call " + bar + "}"

    try:
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            response.write(str(result))

        connection.close()

    except Exception as e:
        response.write("Error processing request.")

    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
