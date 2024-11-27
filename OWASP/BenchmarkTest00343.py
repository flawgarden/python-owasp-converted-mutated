
import os
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00343", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get("BenchmarkTest00343")

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()
        return render_template("results.html", results=results)
    except sqlite3.DatabaseError as e:
        return "Error processing request.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
