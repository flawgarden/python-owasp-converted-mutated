#Snyk original results: [89]
#CodeQL original results: [89]
#Semgrep original results: [89]
#Bandit original results: [89]
#Bearer original results: []
#-------------
#Bearer analysis results: []
#Snyk analysis results: [89]
#CodeQL analysis results: [563]
#Semgrep analysis results: [489, 915, 89, 668]
#Bandit analysis results: [89, 605]
#Original file name: OWASP/BenchmarkTest02545.py
#Original file CWE's: [89]
#Original file kind: fail
#Mutation info: Insert template from /home/zver/IdeaProjects/psi-fuzz/templates-db/languages/python/sensitivity/collections/map.tmt with name map_merge_1_positive
#Used extensions:
#Program:
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

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-05/BenchmarkTest02545", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_post(request)
    return handle_get()

def handle_get():
    return handle_post(request)

def handle_post(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    values = request.form.getlist('BenchmarkTest02545')
    param = values[0] if values else ""

    bar = do_something(request, param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

    try:
        map111 = dict()
        map222 = dict()
        map111["jhdoi"] = bar
        map222[bar] = sql
        map111.update(map222)
        sql = map111[bar]
        conn, cursor = get_sql_statement()
        count = cursor.execute(sql)
        conn.commit()
        output_update_complete(sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def do_something(request, param):
    num = 106
    return param if (7 * 42) - num <= 200 else "This should never happen"

def output_update_complete(sql, response):
    response.data = f"Update complete: {sql}"
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
