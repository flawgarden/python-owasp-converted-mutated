
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor(), conn

@app.route("/sqli-05/BenchmarkTest02454", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()

    response = app.response_class()
    param = request.form.get('BenchmarkTest02454', '')
    bar = do_something(request, param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        statement, conn = get_sql_statement()
        statement.execute(sql)
        conn.commit()
        results = statement.fetchall()
        print_results(sql, results, response)
    except sqlite3.Error as e:
        response = "Error processing request."
        return response

def do_something(request, param):
    return param

def print_results(sql, results, response):
    response.data = f"SQL: {sql}, Results: {results}"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
