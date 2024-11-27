
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('your_database.db')  # Replace with your actual database
    return conn

@app.route("/sqli-02/BenchmarkTest01303", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        param = request.args.get("BenchmarkTest01303", "")
        bar = Test().do_something(request, param)
        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            rows = statement.fetchall()
            print_results(statement, sql)
            connection.close()
        except sqlite3.Error as e:
            return "Error processing request."

    return render_template("index.html")

class Test:

    def do_something(self, request, param):
        bar = "alsosafe"
        if param:
            values_list = ["safe", param, "moresafe"]
            values_list.pop(0)  # remove the 1st safe value
            bar = values_list[1]  # get the last 'safe' value
        return bar

def print_results(statement, sql):
    results = statement.fetchall()
    for row in results:
        print(row)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
