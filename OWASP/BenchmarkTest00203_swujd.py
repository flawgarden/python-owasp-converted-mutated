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

import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00203", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = request.response
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get("BenchmarkTest00203", "")
    param = urllib.parse.unquote(param)

    bar = ""
    num = 106

    bar = "This should never happen" if (7 * 42) - num > 200 else param

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        mc = MagicClass(sql)
        sql = str(mc)
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
        return render_template("success.html", sql=sql)
    except sqlite3.Error as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
