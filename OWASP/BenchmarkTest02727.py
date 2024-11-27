
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')
    return conn

@app.route("/sqli-06/BenchmarkTest02727", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        response = app.response_class(content_type="text/html;charset=UTF-8")

        param = request.args.get("BenchmarkTest02727", "")

        bar = do_something(param)

        sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql, ("foo",))
            results = statement.fetchall()
            connection.commit()
            return print_results(statement, sql, response)
        except sqlite3.Error as e:
            response.set_data("Error processing request.")
            return response

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]  # condition 'B', which is safe

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def print_results(statement, sql, response):
    # Implementation for printing results can be added here
    # This function should format the results and set them into the response
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
