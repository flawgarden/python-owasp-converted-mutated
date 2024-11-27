
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    # Adjust the database connection setup as necessary
    conn = sqlite3.connect('benchmark.db')
    return conn

@app.route("/sqli-00/benchmark-test-00509", methods=['GET', 'POST'])
def benchmark_test_00509():
    if request.method == 'GET':
        return benchmark_test_00509_post()

    return benchmark_test_00509_post()

def benchmark_test_00509_post():
    param = request.args.get('BenchmarkTest00509', '')

    bar = "safe!"
    map94841 = {
        "keyA-94841": "a_Value",
        "keyB-94841": param,
        "keyC": "another_Value"
    }
    bar = map94841["keyB-94841"]
    bar = map94841["keyA-94841"]

    sql = f"{{call {bar}}}"

    try:
        connection = get_sql_connection()
        cursor = connection.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        print_results(results, sql)
    except sqlite3.Error as e:
        print("Error processing request.")
    
    return render_template("index.html")

def print_results(results, sql):
    for row in results:
        print(row)
    # Return results handling as necessary

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
