
import os
import urllib.parse
from flask import Flask, request, render_template, make_response
import sqlite3

app = Flask(__name__, static_url_path='/static', static_folder='static')
app.config['DEBUG'] = True

def get_sql_statement():
    conn = sqlite3.connect('database.db')
    return conn, conn.cursor()

@app.route("/sqli-00/BenchmarkTest00108", methods=['GET'])
def benchmark_test_get():
    response = make_response(render_template("sqli-00/BenchmarkTest00108.html"))
    user_cookie = make_response(response)
    user_cookie.set_cookie("BenchmarkTest00108", "bar", max_age=60 * 3, secure=True, path=request.path, domain=request.host)
    return user_cookie

@app.route("/sqli-00/BenchmarkTest00108", methods=['POST'])
def benchmark_test_post():
    cookies = request.cookies
    param = "noCookieValueSupplied"
    if "BenchmarkTest00108" in cookies:
        param = urllib.parse.unquote(cookies["BenchmarkTest00108"])

    bar = None
    guess = "ABC"
    switch_target = guess[2]

    if switch_target == 'A':
        bar = param
    elif switch_target == 'B':
        bar = "bobs_your_uncle"
    elif switch_target in ('C', 'D'):
        bar = param
    else:
        bar = "bobs_your_uncle"

    sql = "SELECT * FROM USERS WHERE USERNAME='foo' AND PASSWORD='" + bar + "'"
    
    try:
        conn, cursor = get_sql_statement()
        cursor.execute(sql)
        rows = cursor.fetchall()
        # Implement a method to render or display results
        return render_template("results.html", rows=rows)
    except sqlite3.Error as e:
        return "Error processing request.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')
