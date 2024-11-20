
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')  # Replace with your actual database connection
    return conn.cursor()

@app.route("/sqli-00/BenchmarkTest00435", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type="text/html;charset=UTF-8")

    param = request.args.get("BenchmarkTest00435", "")
    bar = "safe!"
    map86691 = {
        "keyA-86691": "a-Value",
        "keyB-86691": param,
        "keyC": "another-Value"
    }
    bar = map86691["keyB-86691"]

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        results = statement.fetchall()
        print_results(sql, results, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def print_results(sql, results, response):
    response.data = f"Query: {sql}, Results: {results}"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
