
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/sqli-02/BenchmarkTest01304", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    else:
        return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(
        response='',
        status=200,
        mimetype='text/html'
    )

    param = request.args.get("BenchmarkTest01304", "")
    bar = Test().do_something(param)

    sql = f"SELECT * from USERS where USERNAME=? and PASSWORD='{bar}'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        return print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response

def print_results(statement, sql, response):
    results = statement.fetchall()
    for row in results:
        response.data += str(row)
    return response

class Test:
    def do_something(self, param):
        bar = ""
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[0]  # get the param value
        return bar

if __name__ == '__main__':
    app.run(host='0.0.0.0')
