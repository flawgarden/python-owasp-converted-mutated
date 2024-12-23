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

import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00018", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = ""
    headers = request.headers.getlist("BenchmarkTest00018")

    if headers:
        param = headers[0]  # just grab first element

    param = urllib.parse.unquote(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + param + "')"

    try:
        set787231 = set()
        set787231.add(sql)
        sql = next(iter(set787231))
        statement = get_sql_statement()
        count = statement.execute(sql)
        statement.connection.commit()
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

def output_update_complete(sql, response):
    response.data = f"Update complete for SQL: {sql}"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
