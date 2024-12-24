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

import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def batch_update(sql):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.close()

@app.route("/sqli-01/BenchmarkTest00846", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return do_post(request)
    return do_post(request)

def do_post(request):
    map787234 = dict()
    map787234["vtpna"] = request
    request = map787234["vtpna"]
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest00846="
    param_loc = query_string.find(paramval)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest00846' in query string."

    param = query_string[param_loc + len(paramval):]

    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = param

    try:
        sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"
        batch_update(sql)
        return f"No results can be displayed for query: {sql}<br> because the batchUpdate method doesn't return results."
    except Exception as e:
        return "Error processing request."

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
