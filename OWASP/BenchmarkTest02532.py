
import os
from flask import Flask, request, render_template
import base64
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02532", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = ""
    values = request.values.getlist("BenchmarkTest02532")
    
    param = values[0] if values else ""
    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = sqlite3.connect('database.db')
        statement = connection.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql, response)
    except sqlite3.Error as e:
        response = "Error processing request."
        print(response)

    return response

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()
    return bar

def print_results(statement, sql, response):
    for row in statement:
        response += str(row)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
