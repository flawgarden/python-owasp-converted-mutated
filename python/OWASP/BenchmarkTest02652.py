
import os
import urllib.parse
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    # Replace with your actual database connection code
    conn = sqlite3.connect('your_database.db')
    return conn.cursor()

@app.route("/sqli-06/BenchmarkTest02652", methods=['GET', 'POST'])
def benchmark_test():
    if request.method == 'GET':
        return benchmark_test_post()    
    return benchmark_test_post()

def benchmark_test_post():
    query_string = request.query_string.decode('utf-8')
    paramval = "BenchmarkTest02652="
    param_loc = query_string.find(paramval)
    
    if param_loc == -1:
        return "getQueryString() couldn't find expected parameter 'BenchmarkTest02652' in query string."

    param = query_string[param_loc + len(paramval):]
    ampersand_loc = query_string.find("&", param_loc)
    if ampersand_loc != -1:
        param = query_string[param_loc + len(paramval):ampersand_loc]

    param = urllib.parse.unquote(param)
    bar = do_something(param)

    sql = f"SELECT * from USERS where USERNAME='foo' and PASSWORD='{bar}'"

    try:
        statement = get_sql_statement()
        statement.execute(sql)
        result = statement.fetchall()
        return render_template("results.html", results=result)
    except sqlite3.Error as e:
        return "Error processing request."

def do_something(param):
    a25323 = param
    b25323 = a25323 + " SafeStuff"
    b25323 = b25323[:-1]  # replace the last character with space
    d25323 = b25323  # take c25323 without the last character
    e25323 = d25323.encode('utf-8').decode('utf-8')
    f25323 = e25323.split(" ")[0]

    # Simulating a call to some external service
    g25323 = "barbarians_at_the_gate"
    return g25323

if __name__ == "__main__":
    app.run(host='0.0.0.0')
