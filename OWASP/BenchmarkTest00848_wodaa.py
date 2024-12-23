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
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Update with your database configuration
    return conn.cursor()

@app.route("/sqli-01/BenchmarkTest00848", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = ""

    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest00848="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00848' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = param
    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"
    list787231 = []
    list787231.append("gpdtk")
    tmp1232141245 = list787231[0]
    list787231[0] = sql
    sql = tmp1232141245

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()
        response = str(results)
    except sqlite3.Error as e:
        response = "Error processing request." if True else str(e)

    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
