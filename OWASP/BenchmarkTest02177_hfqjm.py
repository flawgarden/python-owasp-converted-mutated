#Bearer original results: [89]
#Snyk original results: [89]
#CodeQL original results: [89]
#Bandit original results: [89]
#Semgrep original results: []
#-------------
#Bearer analysis results: [89]
#Snyk analysis results: [89]
#CodeQL analysis results: []
#Semgrep analysis results: [489, 915, 704, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02177.py
#Original file CWE's: [89]  
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/tuples.tmt with name tuple_as_dict_key_positive 
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

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def query_database(sql):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except sqlite3.Error as e:
        return None
    finally:
        conn.close()

@app.route("/sqli-04/BenchmarkTest02177", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest02177", "")
        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
        results = query_database(sql)
        
        if results is not None:
            output = "Your results are: "
            for row in results:
                output += f"{row[0]}<br>"
            return render_template("index.html", output=output)
        else:
            return render_template("index.html", output="No results returned for query: " + sql)

    return render_template("index.html")

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]
    tuple1 = ("aaaa",)
    tuple2 = ("bbbb",)
    my_dict = { (tuple1): param, (tuple2): -26713 }
    param = my_dict[("aaaa",)]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
