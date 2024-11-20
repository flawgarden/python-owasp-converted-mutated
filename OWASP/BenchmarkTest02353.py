
import os
from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('your_database.db')  # Update with your database
    return conn

@app.route("/sqli-05/BenchmarkTest02353", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test()
    return handle_post_request(request)

def handle_post_request(request):
    response = jsonify()
    param = ""
    flag = True
    names = request.form.keys()
    for name in names:
        values = request.form.getlist(name)
        if values is not None:
            for value in values:
                if value == "BenchmarkTest02353":
                    param = name
                    flag = False
                    break
        if not flag:
            break

    bar = do_something(request, param)
    sql = "SELECT * from USERS where USERNAME=? and PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ("foo",))
        results = statement.fetchall()
        print_results(statement, sql, response)
    except sqlite3.Error as e:
        print("Error processing request.")
        return response

def do_something(request, param):
    bar = ""
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

def print_results(statement, sql, response):
    # Implement result printing logic based on your needs
    response.data = str(statement.fetchall())
    response.status_code = 200

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
