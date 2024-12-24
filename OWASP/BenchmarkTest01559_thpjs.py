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

@app.route("/sqli-03/BenchmarkTest01559", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get("BenchmarkTest01559", "")
        bar = do_something(param)

        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        try:
            conn = sqlite3.connect('database.db')
            gen = generator_from(sql, "ntyvg", "bkmer", "aqglg")
            genToList = list(gen)
            sql = genToList[0]
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



def simple_generator(arg1, arg2, arg3):
    yield arg1
    yield arg2
    yield arg3



def infinite_gen(arg1, arg2):
    yield arg1
    while True:
        yield arg2



def generator_from(arg1, arg2, arg3, arg4):
    yield from simple_generator(arg1, arg2, arg3)
    yield arg4
