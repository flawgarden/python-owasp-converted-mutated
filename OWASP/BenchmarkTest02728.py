
import os
import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-06/BenchmarkTest02728", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get("BenchmarkTest02728", None)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')  # Make sure to set your database path
        statement = connection.execute(sql, ("foo",))
        print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

    return response

def do_something(param):
    bar = "safe!"
    map55235 = {}
    map55235["keyA-55235"] = "a-Value"
    map55235["keyB-55235"] = param
    map55235["keyC"] = "another-Value"
    bar = map55235.get("keyB-55235")

    return bar

def print_results(statement, sql, response):
    results = statement.fetchall()
    for row in results:
        response.data += f"<p>{row}</p>"
    response.data += f"<p>Executed SQL: {sql}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
