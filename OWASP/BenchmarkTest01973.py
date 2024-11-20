
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest01973", methods=['GET', 'POST'])
def benchmark_test_01973():
    if request.method == 'GET':
        return benchmark_test_01973_post()
    return benchmark_test_01973_post()

def benchmark_test_01973_post():
    param = request.headers.get("BenchmarkTest01973", "")
    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = f"INSERT INTO users (username, password) VALUES ('foo','{bar}')"

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        output_update_complete(sql)
    except sqlite3.Error as e:
        return "Error processing request."

    return "Request processed successfully."

def do_something(param):
    bar = ""
    guess = "ABC"
    switch_target = guess[1]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bob"
    elif switch_target == 'C' or switch_target == 'D':
        bar = param
    else:
        bar = "bob's your uncle"

    return bar

def output_update_complete(sql):
    return f"Update complete: {sql}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
