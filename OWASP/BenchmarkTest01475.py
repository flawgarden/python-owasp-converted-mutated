
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor(), conn

class ThingInterface:
    @staticmethod
    def doSomething(param):
        return param  # Simulated behavior of the Java interface

class ThingFactory:
    @staticmethod
    def createThing():
        return ThingInterface()

@app.route("/sqli-03/BenchmarkTest01475", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    elif request.method == 'POST':
        return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    for name in request.args:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest01475":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(param)

    sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"

    cursor, conn = get_sql_statement()
    try:
        cursor.execute(sql, (bar,))
        conn.commit()
        return "Update complete"
    except sqlite3.Error as e:
        return "Error processing request.", 500

def do_something(param):
    thing = ThingFactory.createThing()
    return thing.doSomething(param)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
