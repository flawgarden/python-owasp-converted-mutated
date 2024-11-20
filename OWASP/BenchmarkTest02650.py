
from flask import Flask, request, render_template
import urllib.parse
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

@app.route("/sqli-06/BenchmarkTest02650", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    param_val = "BenchmarkTest02650="
    param_loc = query_string.find(param_val)
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02650' in query string."

    param = query_string[param_loc + len(param_val):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(param_val):ampersand_loc]
    param = urllib.parse.unquote(param)

    bar = do_something(request, param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        conn = sqlite3.connect('your_database.db')  # Replace with your database path
        cursor = conn.cursor()
        cursor.execute(sql)
        results = cursor.fetchall()
        conn.close()
        return str(results)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(request, param):
    bar = ""
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ['C', 'D']:
        bar = param
    else:
        bar = "bobs_your_uncle"

    return bar

if __name__ == "__main__":
    app.run(host='0.0.0.0')
