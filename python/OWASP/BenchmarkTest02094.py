
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor(), conn

@app.route("/sqli-04/BenchmarkTest02094", methods=['GET', 'POST'])
def benchmark_test_02094():
    if request.method == 'GET':
        return benchmark_test_02094_post()
    return benchmark_test_02094_post()

def benchmark_test_02094_post():
    param = ""
    headers = request.headers.get("BenchmarkTest02094")

    if headers:
        param = headers  # just grab first element

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement, conn = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()
        conn.commit()
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request.", 500

def do_something(param):
    bar = ""
    num = 196
    if (500 / 42) + num > 200:
        bar = param
    else:
        bar = "This should never happen"
    
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
