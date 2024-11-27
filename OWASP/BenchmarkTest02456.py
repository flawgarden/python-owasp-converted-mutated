
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('your_database.db')
    return conn.cursor()

@app.route("/sqli-05/BenchmarkTest02456", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    response = app.response_class(content_type='text/html;charset=UTF-8')

    param = request.args.get('BenchmarkTest02456', '')
    bar = do_something(param)

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        statement = get_sql_statement()
        count = statement.execute(sql)
        response.data = "Update complete"
        return response
    except sqlite3.Error:
        response.data = "Error processing request."
        return response

def do_something(param):
    bar = None
    num = 86
    if (7 * 42) - num > 200:
        bar = "This_should_always_happen"
    else:
        bar = param
    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
