
import os
import base64
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest01962", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.headers.get('BenchmarkTest01962', '')
    param = param.encode('utf-8').decode('utf-8')

    bar = do_something(param)
    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        print_results(statement, sql)
    except Exception as e:
        return "Error processing request."

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def get_sql_connection():
    # Replace with the actual database connection code
    import sqlite3
    return sqlite3.connect('your_database.db')

def print_results(statement, sql):
    # Replace with actual result printing logic
    results = statement.fetchall()
    for row in results:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
