#Snyk original results: [89]
#Bearer original results: [89]
#CodeQL original results: [89]
#Bandit original results: [89]
#Semgrep original results: []
#-------------
#Snyk analysis results: [79, 1004]
#Bearer analysis results: [1004]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 614, 915, 704, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest01882.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/stepanov/f/psi-fuzz/templates-db/languages/python/sensitivity/collections/queue.tmt with name simple_peek_negative 
#Used extensions: MACRO_Create_Queue -> ~[MACRO_QueueName]~ = SimpleQueue() | MACRO_Add_Fixed_VAR_ToQueue -> ~[MACRO_QueueName]~.put_nowait(~[VAR_~[TYPE@1]~@1]~) | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231 | MACRO_QueueName -> queue787231
#Program:
from queue import SimpleQueue, Queue, PriorityQueue
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

from flask import Flask, request, render_template, make_response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_db(sql):
    conn = sqlite3.connect('database.db')  # Adjust your database connection
    queue787231 = SimpleQueue()
    queue787231.put_nowait(sql)
    queue787231.get()
    sql = queue787231.get_nowait()
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results

@app.route("/sqli-04/BenchmarkTest01882", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        response = make_response(render_template("sqli-04/BenchmarkTest01882.html"))
        user_cookie = ('BenchmarkTest01882', 'bar', 60 * 3, True)  # cookie name, value, max age, secure
        response.set_cookie(user_cookie[0], user_cookie[1], max_age=user_cookie[2], secure=user_cookie[3], path=request.path)
        return response

    if request.method == 'POST':
        cookies = request.cookies
        param = "noCookieValueSupplied"
        if 'BenchmarkTest01882' in cookies:
            param = urllib.parse.unquote(cookies['BenchmarkTest01882'])

        bar = do_something(param)
        
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        try:
            results = query_db(sql)
            output = "Your results are:<br>"
            for result in results:
                output += f"{result[0]}<br>"  # Assuming USERNAME is the first column
            return output
        except Exception as e:
            return "Error processing request."

def do_something(param):
    bar = "safe!"
    map67948 = {
        "keyA-67948": "a-Value",
        "keyB-67948": param,
        "keyC": "another-Value"
    }
    bar = map67948["keyB-67948"]
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
