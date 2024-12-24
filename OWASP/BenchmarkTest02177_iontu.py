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
tmpUnique42 = app
match app:
    case "mmmoz":
        pass
    case "drota":
        app = app
    case _:
        app = tmpUnique42

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
