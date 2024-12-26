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

import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-02/BenchmarkTest01382", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest01382', '')
        bar = Test().do_something(param)
        sh = StringHolder()
        bar = sh.value

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            cursor.execute(sql, ("foo",))
            results = cursor.fetchall()
            return render_template("results.html", results=results)
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
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')