import string
from string import capwords
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
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True


@app.route("/sqli-02/BenchmarkTest01090", methods=['POST', 'GET'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.headers.get("BenchmarkTest01090", "")
    param = urllib.parse.unquote(param)
    MonkeyClass.getArg = newGetArg
    tmpInstance = MonkeyClass(param)
    param = tmpInstance.getArg()

    bar = Test().do_something(request, param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.commit()
        print_results(sql, results)
    except sqlite3.Error:
        return "Error processing request.", 500

def print_results(sql, results):
    print("SQL: ", sql)
    print("Results: ", results)

class Test:

    def do_something(self, request, param):
        bar = "safe!"
        map_holder = {}
        map_holder["keyA-12212"] = "a-Value"
        map_holder["keyB-12212"] = param
        map_holder["keyC"] = "another-Value"
        bar = map_holder.get("keyB-12212")
        return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')




def newGetArg(self):
    return "fixed_string"





def newGetArgWithArg(self, arg):
    return self.arg + arg





def mock_capwords(s, sep=None):
    return "FIXED_STRING"





def new_arg(arg):
    return arg
