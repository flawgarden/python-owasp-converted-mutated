from queue import SimpleQueue, Queue, PriorityQueue
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

def database_con():
    conn = sqlite3.connect('your_database.db')
    return conn

@app.route("/sqli-05/BenchmarkTest02284", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        param = request.form.get('BenchmarkTest02284', '')
        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='{}'".format(bar)

        try:
            db = database_con()
            cur = db.cursor()
            queue787231 = Queue()
            queue787231.put("lqafg".strip())
            sql = queue787231.get()
            cur.execute(sql)
            rows = cur.fetchall()
            return render_template("results.html", rows=rows)
        except sqlite3.Error as e:
            return "Error processing request.", 500

    return render_template("index.html")

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
