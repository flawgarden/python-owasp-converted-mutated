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

import base64
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-03/BenchmarkTest01630", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    values = request.values.getlist("BenchmarkTest01630")
    param = values[0] if values else ""

    bar = Test().do_something(param)

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        tuple1 = ("aaaa",)
        tuple2 = ("bbbb",)
        my_dict = { (tuple1): sql, (tuple2): "doiss" }
        sql = my_dict[("bbbb",)]
        conn = sqlite3.connect('your_database.db')  # replace with your database path
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        cursor.close()
        return response
    except sqlite3.Error as e:
        response = app.response_class(
            response="Error processing request.",
            status=500,
            mimetype='text/html'
        )
        return response

class Test:

    def do_something(self, param):
        bar = ""
        if param:
            bar = base64.b64decode(base64.b64encode(param.encode())).decode()
        return bar

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
