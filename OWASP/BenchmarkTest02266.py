
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    return sqlite3.connect('your_database.db')

@app.route("/sqli-04/BenchmarkTest02266", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST' or request.method == 'GET':
        response = app.response_class(content_type='text/html;charset=UTF-8')

        param = ""
        if request.args:
            param = request.args.get('BenchmarkTest02266', '')

        bar = do_something(request, param)

        sql = "{call " + bar + "}"

        try:
            connection = get_sql_connection()
            statement = connection.cursor()
            statement.execute(sql)
            results = statement.fetchall()
            print_results(results, sql, response)
        except sqlite3.Error as e:
            response.data = "Error processing request."
            return response
        return response

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def print_results(results, sql, response):
    result_str = f"SQL: {sql}\n"
    for row in results:
        result_str += str(row) + "\n"
    response.data = result_str

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
