
import os
from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-05/BenchmarkTest02354", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = jsonify()
    param = ""
    flag = True
    names = request.args.keys()

    for name in names:
        values = request.args.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02354":
                    param = name
                    flag = False
                    break

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        response = print_results(statement, sql)
        connection.commit()
    except Exception as e:
        response = "Error processing request."

    return response

def do_something(param):
    bar = ""
    num = 106
    bar = "This should never happen" if (7 * 42) - num > 200 else param
    return bar

def get_sql_connection():
    # Dummy function for acquiring a SQL connection
    import sqlite3
    return sqlite3.connect('your_database.db')

def print_results(statement, sql):
    # Dummy function to mock the printing of SQL results
    results = statement.fetchall()
    return jsonify(results)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
