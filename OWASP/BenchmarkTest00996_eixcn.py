#CodeQL original results: [89]
#Semgrep original results: [89]
#Snyk original results: []
#Bearer original results: []
#Bandit original results: []
#-------------
#Snyk analysis results: [1004]
#Bearer analysis results: [1004]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 614, 89, 668]
#Bandit analysis results: [605]
#Original file name: OWASP/BenchmarkTest00996.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_merge_1_positive 
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

import base64
import sqlite3
from flask import Flask, request, make_response, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest00996", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-02/BenchmarkTest00996.html"))
        user_cookie = base64.b64encode(b"verifyUserPassword('foo','bar')").decode('utf-8')
        response.set_cookie("BenchmarkTest00996", user_cookie, max_age=60 * 3, secure=True, path=request.path, domain=request.host)
        return response
    else:
        param = request.cookies.get("BenchmarkTest00996", "noCookieValueSupplied")
        bar = Test().do_something(param)

        sql = "{call " + bar + "}"

        try:
            map111 = dict()
            map222 = dict()
            map111["vzqpp"] = param
            map222["hjytb"] = sql
            map111.update(map222)
            sql = map111["hjytb"]
            connection = sqlite3.connect('database.db')  # Adjust with actual DB connection
            cursor = connection.cursor()
            cursor.execute(sql)
            rows = cursor.fetchall()
            for row in rows:
                print(row)  # Use rendering to display instead of print as required
            connection.close()

        except sqlite3.Error as e:
            return "Error processing request.", 500

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode('utf-8'))).decode('utf-8')
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
