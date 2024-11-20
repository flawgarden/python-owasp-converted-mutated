
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-04/BenchmarkTest02098", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()

    return benchmark_test_post()

def benchmark_test_post():
    param = ""
    headers = request.headers.get('BenchmarkTest02098')

    if headers:
        param = headers

    param = urllib.parse.unquote(param)

    bar = do_something(param)

    sql = "SELECT * from USERS where USERNAME='foo' and PASSWORD='" + bar + "'"

    try:
        conn = sqlite3.connect('database.db')  # Update with your database path
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        return print_results(results, sql)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
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

    return bar

def print_results(results, sql):
    response = "<h1>Results:</h1>"
    for row in results:
        response += f"<p>{row}</p>"
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0')
