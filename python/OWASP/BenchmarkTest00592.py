
import os
from flask import Flask, request, render_template
from base64 import b64encode, b64decode
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-01/BenchmarkTest00592", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    flag = True
    names = request.args  # Alternatively request.form for POST
    for name in names:
        values = request.args.getlist(name)
        if values:
            for value in values:
                if value == "BenchmarkTest00592":
                    param = name
                    flag = False
                    break

    a36502 = param
    b36502 = a36502 + " SafeStuff"
    b36502 = b36502[:-len("Chars")] + "Chars"
    
    map36502 = {"key36502": b36502}
    c36502 = map36502["key36502"]
    d36502 = c36502[:-1]
    e36502 = b64decode(b64encode(d36502.encode())).decode()

    f36502 = e36502.split(" ")[0]
    g36502 = "barbarians_at_the_gate"
    bar = do_something(g36502)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.execute(sql, ("foo",))
        print_results(statement, sql)
    except Exception as e:
        return "Error processing request."

def do_something(g):
    # Mock implementation of the ThingInterface's doSomething method.
    return g

def get_sql_connection():
    # Mock implementation of getting an SQLite connection.
    return sqlite3.connect('example.db')

def print_results(statement, sql):
    # Mock implementation of printing results.
    results = statement.fetchall()
    for row in results:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
