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

@app.route("/sqli-02/BenchmarkTest01097", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.headers.get("BenchmarkTest01097", "")
        param = urllib.parse.unquote(param)

        bar = Test().do_something(param)

        sql = "INSERT INTO users (username, password) VALUES ('foo','{}')".format(bar)

        try:
            conn = sqlite3.connect('database.db')  # replace with your database connection
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            cursor.close()
            conn.close()
            return "Update complete", 200
        except sqlite3.Error as e:
            return "Error processing request.", 500

    return render_template("index.html")

class Test:
    def do_something(self, param):
        bar = ""

        num = 196
        if (500 / 42) + num > 200:
            bar = param
        else:
            bar = "This should never happen"
        list787231 = []
        list787231.append("ipdsp")
        bar = list(list787231)[0]

        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
