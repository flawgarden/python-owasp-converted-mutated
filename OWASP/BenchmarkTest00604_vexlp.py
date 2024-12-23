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

import base64
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')  # Adjust your database path
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00604", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00604":
                    param = name
                    flag = False
                    mc = MagicClass("lnvts")
                    param = mc.arg
                    break

    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        rs = cursor.fetchall()
        # Replace with your method to print results
        # print_results(rs, sql, response)
        conn.close()
        return response
    except sqlite3.Error as e:
        if True:  # Adjust error handling as needed
            response.data = "Error processing request."
            return response
        else:
            raise

if __name__ == "__main__":
    app.run(host='0.0.0.0')
