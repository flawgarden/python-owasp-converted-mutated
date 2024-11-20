
import os
from flask import Flask, request, render_template, Response
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    # Replace with your actual database connection logic
    return sqlite3.connect('database.db')

@app.route("/sqli-04/BenchmarkTest01969", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    response.headers['Content-Type'] = 'text/html;charset=UTF-8'

    param = request.headers.get('BenchmarkTest01969', '')
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        cursor = statement.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        # Replace with your actual result handling logic
        print(result)
        response.set_data("Results processed.")
    except sqlite3.Error as e:
        response.set_data("Error processing request.")
        return response

    return response

def do_something(param):
    num = 106
    return "This_should_always_happen" if (7 * 18) + num > 200 else param

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
