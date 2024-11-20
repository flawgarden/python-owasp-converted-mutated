
import base64
import os
from flask import Flask, request, render_template, Response
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

def output_update_complete(sql, response):
    response.write(f"Executed SQL: {sql}")

@app.route("/sqli-04/BenchmarkTest02099", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    response = Response()
    param = request.headers.get("BenchmarkTest02099", "")

    param = base64.b64decode(base64.b64encode(param.encode())).decode()

    bar = do_something(param)

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        db, cur = get_sql_statement()
        count = cur.execute(sql)
        output_update_complete(sql, response)
        db.commit()
    except sqlite3.Error as e:
        response.write("Error processing request.")
        return response

    return response

def do_something(param):
    bar = ""
    if param:
        bar = base64.b64decode(base64.b64encode(param.encode())).decode()

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
