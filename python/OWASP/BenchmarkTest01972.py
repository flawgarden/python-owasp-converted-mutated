
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor()

def print_results(statement, sql, response):
    results = statement.fetchall()
    for row in results:
        response.get_writer().write(str(row))

@app.route("/sqli-04/BenchmarkTest01972", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class()
    param = request.headers.get("BenchmarkTest01972", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        print_results(statement, sql, response)
    except sqlite3.DatabaseError as e:
        response.set_data("Error processing request.")
        return response

def do_something(param):
    bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
