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

@app.route("/sqli-03/BenchmarkTest01559", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01559", "")
        bar = do_something(param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        try:
            tmpArrayUnique42 = ["", ""]
            tmpArrayUnique42[0] = sql
            ah = ArrayHolder(values=tmpArrayUnique42)
            sql = ah.values[1]
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            conn.close()
            return render_template("result.html", results=results)
        except sqlite3.Error as e:
            return "Error processing request.", 500
    return render_template("benchmark_test.html")

def do_something(param):
    bar = "safe!"
    map_ = {
        "keyA-31651": "a-Value",
        "keyB-31651": param,
        "keyC": "another-Value"
    }
    bar = map_.get("keyB-31651")
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
