
import os
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-00/BenchmarkTest00429", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00429', "")
    bar = ""

    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.execute(sql, ("foo",))
        values = statement.fetchall()
        print_results(statement, sql)
    except sqlite3.Error as e:
        return "Error processing request."

    return render_template("index.html")

def print_results(statement, sql):
    # Implement result printing logic here
    pass

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
