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
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00192", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()

    param = request.headers.get("BenchmarkTest00192", "")
    param = urllib.parse.unquote(param)

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('path_to_your_database.db')
        map787234 = dict()
        map787234[sql] = "thiku"
        map787234[sql] = sql
        if sql in map787234:
            map787234.update({sql: "avnkc"})
        sql = map787234[sql]
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        if True:  # substitute with a condition to hide SQL errors
            response.data = "Error processing request."
            response.status_code = 500
            return response
        else:
            raise e

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
