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

def query_database(sql):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        result = cursor.fetchone()
        return result
    except Exception as e:
        return None
    finally:
        conn.close()

@app.route("/sqli-04/BenchmarkTest02181", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    param = request.form.get('BenchmarkTest02181', '')
    bar = do_something(request, param)

    sql = f"SELECT userid FROM USERS WHERE USERNAME='foo' AND PASSWORD='{bar}' LIMIT 1"
    try:
        result = query_database(sql)
        return f"Your results are: {result}" if result else "No results returned for query."
    except Exception as e:
        return "Error processing request."

def do_something(request, param):
    set787231 = set()
    set787231.add("ztqfn")
    set787231.add(param)
    set787231.remove(param)
    param = next(iter(set787231))
    return param

if __name__ == '__main__':
    app.run(host='0.0.0.0')
