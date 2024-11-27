
import urllib.parse
import os
from flask import Flask, request, render_template, Response
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    return sqlite3.connect('database.db')

@app.route("/sqli-05/BenchmarkTest02631", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode()
    paramval = "BenchmarkTest02631="
    param_loc = query_string.find(paramval)

    if param_loc == -1:
        return Response("getQueryString() couldn't find expected parameter 'BenchmarkTest02631' in query string.", status=400)

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)

    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)
    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(results, sql)
        connection.close()
    except sqlite3.Error as e:
        return Response("Error processing request.", status=500)

def do_something(param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

def print_results(results, sql):
    # Placeholder for result printing; implement as needed
    print(f"SQL: {sql}")
    print(f"Results: {results}")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
