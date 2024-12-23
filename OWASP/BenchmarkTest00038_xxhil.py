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

@app.route("/sqli-00/BenchmarkTest00038", methods=['GET', 'POST'])
def benchmark_test_00038():
    if request.method == 'GET':
        return benchmark_test_00038_post()
    return benchmark_test_00038_post()

def benchmark_test_00038_post():
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00038":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    sql = "SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='" + param + "'"

    try:
        map787234 = dict()
        map787234[names] = "zngvv"
        map787234.setdefault(names, sql)
        sql = map787234[names]
        conn = sqlite3.connect('your_database.db')  # Change to your database
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()

        response = "Your results are:<br>"
        for row in results:
            response += escape_html(row[0]) + "<br>"
        return response

    except sqlite3.Error as e:
        return "No results returned for query: " + escape_html(sql)

def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
