
import os
import urllib.parse
from flask import Flask, request, render_template
import sqlite3
from base64 import b64encode, b64decode

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest01961", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest01961", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql, ('foo',))
        results = cursor.fetchall()
        print_results(cursor, sql)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    a99523 = param
    b99523 = a99523 + " SafeStuff"
    b99523 = b99523[:-len("Chars")] + "Chars"
    map99523 = {}
    map99523["key99523"] = b99523
    c99523 = map99523["key99523"]
    d99523 = c99523[:-1]
    e99523 = b64decode(b64encode(d99523.encode())).decode()
    f99523 = e99523.split(" ")[0]
    thing = create_thing()
    g99523 = "barbarians_at_the_gate"
    bar = thing.do_something(g99523)

    return bar

def get_sql_connection():
    conn = sqlite3.connect('example.db')  # replace with your database
    return conn

def print_results(cursor, sql):
    # Function to print the results
    for row in cursor.fetchall():
        print(row)

class ThingInterface:
    def do_something(self, value):
        return value

def create_thing():
    return ThingInterface()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
