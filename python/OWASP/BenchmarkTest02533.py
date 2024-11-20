
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    # Implement your database connection logic here
    return sqlite3.connect('database.db')

@app.route("/sqli-05/BenchmarkTest02533", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        response = app.response_class(content_type='text/html;charset=UTF-8')
        values = request.form.getlist("BenchmarkTest02533")
        param = values[0] if values else ""

        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            print_results(statement, sql, response)
            return response
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response
    return render_template("index.html")

def do_something(param):
    bar = ""
    if param:
        values_list = ["safe", param, "moresafe"]
        values_list.pop(0)  # remove the 1st safe value
        bar = values_list[0]  # get the param value
    return bar

def print_results(statement, sql, response):
    # Implement your result printing logic here
    pass

if __name__ == "__main__":
    app.run(host='0.0.0.0')
