
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    # Assuming a function to create a DB connection exists
    conn = sqlite3.connect('your_database.db')
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00438", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_logic()
    elif request.method == 'POST':
        return benchmark_test_logic()

def benchmark_test_logic():
    param = request.values.get("BenchmarkTest00438", "")
    bar = ""

    num = 106
    bar = (7 * 42) - num > 200 and "This should never happen" or param

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        rows = statement.fetchall()
        return render_template("results.html", results=rows)
    except sqlite3.Error as e:
        return "Error processing request." if True else str(e)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
