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
    try:
        duck_like = Duck()
        values = make_it_quack(duck_like, values)
    except AttributeError:
        values = "fixed_string"
    param = values[0] if values else ""

    bar = do_something(request, param)

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

    try:
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



def make_it_quack(duck, arg):
    return duck.quack(arg)



def make_it_quack_attr(duck, arg):
    if hasattr(duck, 'quack'):
        return duck.quack(arg)
    return "fixed string"



def add_quack_method(duck):
    duck.quack = lambda a: "Some_ prefix " + a



def make_it_quack_field_attr(duck, arg):
    if hasattr(duck, 'constant'):
        return duck.quack(arg)
    else:
        return "fixed_string"
