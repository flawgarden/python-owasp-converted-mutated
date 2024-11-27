
from flask import Flask, request, render_template
import sqlite3
import os

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_connection():
    conn = sqlite3.connect('database.db')  # Adjust your database path
    return conn

@app.route("/sqli-05/BenchmarkTest02450", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'POST':
        return handle_request(request)
    return handle_request(request)

def handle_request(request):
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02450', '')
    bar = do_something(request, param)

    sql = "SELECT * FROM USERS WHERE USERNAME=? AND PASSWORD='" + bar + "'"

    try:
        connection = get_sql_connection()
        statement = connection.cursor()
        statement.execute(sql, ('foo',))
        print_results(statement, sql, response)
    except sqlite3.Error as e:
        response.data = "Error processing request."
        return response
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
    results = statement.fetchall()
    for row in results:
        response.data += f"<p>{row}</p>"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0')
