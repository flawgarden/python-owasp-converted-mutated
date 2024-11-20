
import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn.cursor(), conn

@app.route("/sqli-01/BenchmarkTest00774", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    values = request.args.getlist("BenchmarkTest00774")
    param = values[0] if values else ""

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

    sql = "INSERT INTO users (username, password) VALUES ('foo', ?)"

    try:
        statement, conn = get_sql_statement()
        statement.execute(sql, (bar,))
        conn.commit()
        # Assuming outputUpdateComplete is a function to send response back
        output_update_complete(sql)
    except sqlite3.Error as e:
        # Handle error
        return "Error processing request."

def output_update_complete(sql):
    # You can modify this function to render a template or return a message
    return f"SQL Update Complete: {sql}"

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
