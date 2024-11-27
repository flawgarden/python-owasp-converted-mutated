
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-01/BenchmarkTest00682", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = request.args.get("BenchmarkTest00682", "")
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

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        conn.commit()
        return "Update complete"
    except sqlite3.DatabaseError as e:
        if True:  # Hide SQL errors
            return "Error processing request."
        else:
            raise

if __name__ == "__main__":
    app.run(host='0.0.0.0')
