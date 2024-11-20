
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # replace with your database path
    return conn.cursor()

@app.route("/sqli-01/BenchmarkTest00515", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get('BenchmarkTest00515', default='', type=str)

    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()  # Fetch results
        return render_template("results.html", results=results)
    except sqlite3.Error as e:
        return "Error processing request."

if __name__ == "__main__":
    app.run(host='0.0.0.0')
