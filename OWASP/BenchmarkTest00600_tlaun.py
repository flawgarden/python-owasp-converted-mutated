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

@app.route("/sqli-01/BenchmarkTest00600", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args.keys()
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00600":
                    param = name
                    flag = False

    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target in ['A', 'C', 'D']:
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    map787234 = dict()
    map787234["iwuyc"] = bar
    if "iwuyc" in map787234:
        bar = map787234.pop("iwuyc")
    else:
        bar = "bobs_your_uncle"

    try:
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        # Simulating a DB operation
        connection = sqlite3.connect('example.db')  # Replace with actual DB connection
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        connection.close()

        return f"No results can be displayed for query: {sql}<br> because the execution method doesn't return results."
    except Exception as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
