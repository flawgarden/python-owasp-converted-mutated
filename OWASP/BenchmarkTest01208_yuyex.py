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

@app.route("/sqli-02/BenchmarkTest01208", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01208", "")
    tmpList = [param, "ovowi", "olyvw"]
    compList = [x for x in tmpList if "prefix" in x]
    param = compList[0]
    param = urllib.parse.unquote(param)

    bar = Test().do_something(param)

    sql = f"{{call {bar}}}"

    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql)
        connection.close()
    except sqlite3.Error as e:
        return "Error processing request."

class Test:
    def do_something(self, param):
        num = 106
        bar = "This should never happen" if (7 * 42) - num > 200 else param
        return bar

def print_results(results, sql):
    for row in results:
        print(row)  # or process results as needed

if __name__ == "__main__":
    app.run(host='0.0.0.0')
