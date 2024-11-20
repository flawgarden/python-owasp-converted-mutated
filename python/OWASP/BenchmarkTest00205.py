
import os
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Update with your database path
    return conn.cursor(), conn

@app.route("/sqli-00/BenchmarkTest00205", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get("BenchmarkTest00205", "")
    param = urllib.parse.unquote(param)

    bar = "alsosafe"
    if param:
        values_list = []
        values_list.append("safe")
        values_list.append(param)
        values_list.append("moresafe")

        values_list.pop(0)

        bar = values_list[1]

    sql = "INSERT INTO users (username, password) VALUES ('foo','" + bar + "')"

    try:
        statement, conn = get_sql_statement()
        count = statement.execute(sql)
        conn.commit()
        return "Update complete", 200
    except sqlite3.Error as e:
        if True:  # You can change this condition to control error hiding
            return "Error processing request.", 500
        else:
            raise

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
