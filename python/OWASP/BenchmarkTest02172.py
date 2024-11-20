
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')  # Update with your database path
    return conn

@app.route("/sqli-04/BenchmarkTest02172", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return process_request()

    return render_template("index.html")

def process_request():
    param = request.form.get("BenchmarkTest02172", "")
    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.execute(sql, ("foo",))
        results = statement.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    num = 106
    return "This_should_always_happen" if (7 * 18) + num > 200 else param

if __name__ == "__main__":
    app.run(host='0.0.0.0')
